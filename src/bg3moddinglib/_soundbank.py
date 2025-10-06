from __future__ import annotations

import copy
import os.path
import xml.etree.ElementTree as et

from ._common import get_required_bg3_attribute, lower_bound_by_bg3_attribute, set_bg3_attribute
from ._files import game_file, game_files
from ._speakers import SPEAKER_NARRATOR

class soundbank_asset:
    __wem_path: str
    __ffxanim_path: str
    __gr2_path: str

    def __init__(self, wem_path: str, ffxanim_path: str, gr2_path: str) -> None:
        self.__wem_path = wem_path
        self.__ffxanim_path = ffxanim_path
        self.__gr2_path = gr2_path

    @property
    def wem_path(self) -> str:
        return self.__wem_path
    
    @property
    def ffxanim_path(self) -> str:
        return self.__ffxanim_path

    @property
    def gr2_path(self) -> str:
        return self.__gr2_path


class soundbank_object:
    __file: game_file
    __soundbank_id: str
    __speaker_id: str
    __index: dict[str, tuple[str, str]]

    def __init__(self, gamefile: game_file) -> None:
        self.__file = gamefile
        self.__index = dict[str, tuple[str, str]]()
        if gamefile.relative_file_path.endswith('.lsf'):
            self.__soundbank_id = os.path.basename(gamefile.relative_file_path)[:-4]
        else:
            raise RuntimeError(f'expected an .lsf file, but got {gamefile.relative_file_path}')
        speaker_metadata = gamefile.xml.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]')
        if speaker_metadata is None:
            raise RuntimeError(f'not a sound bank: {gamefile.relative_file_path}')
        self.__speaker_id = get_required_bg3_attribute(speaker_metadata, 'MapKey')


    @staticmethod
    def create_new(files: game_files, speaker: str) -> soundbank_object:
        if speaker == SPEAKER_NARRATOR:
            speaker = 'NARRATOR'
        filename = speaker.replace('-', '')
        soundbank_file = files.add_new_file(f'Mods/ModNameHere/Localization/English/Soundbanks/{filename}.lsf', is_mod_specific = True)
        root_node = soundbank_file.root_node
        root_node.append(et.fromstring('<version major="3" minor="2" revision="0" build="0" lslib_meta="v1,bswap_guids" />'))
        root_node.append(et.fromstring(''.join((
            '<region id="VoiceMetaData">',
            '<node id="VoiceMetaData">',
            '<children>',
            '<node id="VoiceSpeakerMetaData">',
            f'<attribute id="MapKey" type="FixedString" value="{speaker}" />',
            '<children>',
            '<node id="MapValue">',
            '<children>',
            '</children>',
            '</node>',
            '</children>',
            '</node>',
            '</children>',
            '</node>',
            '</region>'
        ))))
        return soundbank_object(soundbank_file)

    @property
    def file(self) -> game_file:
        return self.__file

    @property
    def soundbank_id(self) -> str:
        return self.__soundbank_id

    @property
    def speaker_id(self) -> str:
        return self.__speaker_id

    def merge_voice_metadata_from_file(self, gf: game_file) -> None:
        parent_node = self.__file.root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children')
        if parent_node is None:
            raise ValueError(f"cannot parse {self.__file.relative_file_path} as a soundbank file")
        nodes = gf.root_node.findall('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children/node[@id="VoiceTextMetaData"]')
        for node in nodes:
            cnode = copy.copy(node)
            parent_node.append(cnode)
            handle = get_required_bg3_attribute(cnode, 'MapKey')
            value = cnode.find('./children/node[@id="MapValue"]')
            if value is None:
                raise ValueError(f'malformed entry with handle {handle}')
            source = get_required_bg3_attribute(value, 'Source')
            duration = get_required_bg3_attribute(value, 'Length')
            self.__index[handle] = (source, duration)

    def add_voice_metadata(self, text_handle: str, duration: float | str, audio_file_name: str | None = None) -> None:
        root_node = self.__file.root_node
        parent_node = root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children')
        if parent_node is None:
            raise ValueError(f"cannot parse {self.__file.relative_file_path} as a soundbank file")
        nodes = parent_node.findall('./node[@id="VoiceTextMetaData"]')
        if len(nodes) > 0:
            index = lower_bound_by_bg3_attribute(nodes, "MapKey", text_handle)
        else:
            index = 0
        if audio_file_name is None:
            audio_file_name = f'v{self.__soundbank_id}_{text_handle}.wem'
        new_node = et.fromstring(f"""\n<node id="VoiceTextMetaData">
            <attribute id="MapKey" type="FixedString" value="{text_handle}" />
            <children>
                <node id="MapValue">
                    <attribute id="Codec" type="FixedString" value="VORBIS" />
                    <attribute id="Length" type="float" value="{duration}" />
                    <attribute id="Priority" type="FixedString" value="P1_StoryDialog" />
                    <attribute id="Source" type="FixedString" value="{audio_file_name}" />
                </node>
            </children>
        </node>\n""")
        parent_node.insert(index, new_node)

    def delete_voice_metadata(self, text_handle: str) -> None:
        root_node = self.__file.root_node
        parent_node = root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children')
        if parent_node is not None:
            nodes = parent_node.findall('./node[@id="VoiceTextMetaData"]')
            index = lower_bound_by_bg3_attribute(nodes, "MapKey", text_handle)
            if get_required_bg3_attribute(nodes[index], "MapKey") == text_handle:
                parent_node.remove(nodes[index])
                return
        raise KeyError(f"node {text_handle} doesn't exist in soundbank {self.__file.relative_file_path}")

    def update_voice_metadata(self, text_handle: str, duration: float, audio_file_name: str) -> None:
        root_node = self.__file.root_node
        parent_node = root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children')
        if parent_node is not None:
            nodes = parent_node.findall('./node[@id="VoiceTextMetaData"]')
            index = lower_bound_by_bg3_attribute(nodes, "MapKey", text_handle)
            node = nodes[index]
            if get_required_bg3_attribute(node, "MapKey") == text_handle:
                node = node.find('./children/node[@id="MapValue"]')
                if node is None:
                    raise ValueError(f"bad node {text_handle} in soundbank {self.__file.relative_file_path}, update failed")
                set_bg3_attribute(node, "Length", str(duration))
                set_bg3_attribute(node, "Source", audio_file_name)
        raise KeyError(f"node {text_handle} doesn't exist in soundbank {self.__file.relative_file_path}")

    def get_wem_file_name(self, text_handle: str) -> str:
        if len(self.__index) == 0:
            self.__build_index()
        if text_handle in self.__index:
            return self.__index[text_handle][0]
        raise KeyError(f'soundbank entry not found for the given handle {text_handle}')

    def get_duration(self, text_handle: str) -> str:
        if len(self.__index) == 0:
            self.__build_index()
        if text_handle in self.__index:
            return self.__index[text_handle][1]
        raise KeyError(f'soundbank entry not found for the given handle {text_handle}')

    def unpack_sound_assets(self, text_handle: str) -> soundbank_asset:
        wem_file_name = self.get_wem_file_name(text_handle)
        base_file_name = wem_file_name.split('.')[0]
        gf_wem = game_file(
            self.__file.tool,
            'Mods/Gustav/Localization/English/Soundbanks/' + wem_file_name,
            pak_name='Localization/Voice')
        gf_ffxanim = game_file(
            self.__file.tool,
            'Mods/Gustav/Localization/English/Animation/' + f'FX_{base_file_name}.ffxanim',
            pak_name='Localization/English_Animations')
        gf_gr2 = game_file(
            self.__file.tool,
            'Mods/Gustav/Localization/English/Animation/' + f'MC_{base_file_name}.gr2',
            pak_name='Localization/English_Animations')
        return soundbank_asset(gf_wem.unpacked_file_path, gf_ffxanim.unpacked_file_path, gf_gr2.unpacked_file_path)

    def get_all_text_handles(self) -> tuple[str, ...]:
        if len(self.__index) == 0:
            self.__build_index()
        return tuple(self.__index.keys())

    def __build_index(self) -> None:
        nodes = self.__file.root_node.findall('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children/node[@id="VoiceTextMetaData"]')
        if len(nodes) == 0:
            raise RuntimeError(f'not a soundbank or an empty soundbank: {self.__file.relative_file_path}')
        for node in nodes:
            handle = get_required_bg3_attribute(node, 'MapKey')
            value = node.find('./children/node[@id="MapValue"]')
            if value is None:
                raise ValueError(f'malformed entry with handle {handle}')
            source = get_required_bg3_attribute(value, 'Source')
            duration = get_required_bg3_attribute(value, 'Length')
            self.__index[handle] = (source, duration)
        
