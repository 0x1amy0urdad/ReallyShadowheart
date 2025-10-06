from __future__ import annotations

import json
import os
import os.path
import traceback
import xml.etree.ElementTree as et

from ._assets import bg3_assets
from ._common import get_bg3_attribute
from ._constants import SPEAKER_NARRATOR
from ._files import game_file, game_files
from ._dialog import dialog_object
from ._soundbank import soundbank_object
from ._tool import bg3_modding_tool

from typing import Callable, Iterable

class dialog_scanner:
    __assets: bg3_assets
    __line_count: dict[str, int]

    def __init__(self, tool: bg3_modding_tool) -> None:
        self.__assets = bg3_assets(game_files(tool, "scanner", "00000000-0000-0000-0000-000000000000"))
        self.__line_count = dict[str, int]()

    def scan_dialogs(self, on_dialog_node: Callable[[dialog_object], None], /, early_access: bool = False) -> None:
        # if early_access:
        #     files = [f for f in self.__assets.tool.list(pak_file_name) if f.endswith('.lsj') and 'Dialogs' in f]
        # else:
        #     files = [f for f in self.__assets.tool.list(pak_file_name) if f.endswith('.lsf') and 'DialogsBinary' in f]
        files = self.__assets.index.get_dialogs_paths()
        scanner_progress_file_path = os.path.join(os.getcwd(), "__scanner__", "scanner_progress")
        files_count = len(files)
        n = 0
        for pak, file in files:
            try:
                gf = game_file(self.__assets.tool, file, pak_name = pak)
                dialog = dialog_object(gf)
                on_dialog_node(dialog)
            except BaseException:
                exc = traceback.format_exc()
                print(f"Skipped {file} because processing failed due to exception: \n{exc}")
            n += 1
            if n % 10 == 0:
                with open(scanner_progress_file_path, "wt") as fd:
                    fd.write(f"progress: {n} / {files_count}\n")

    def create_voice_lines_index(self, speakers_uuids: list[str], /, early_access: bool = False) -> None:
        if SPEAKER_NARRATOR in speakers_uuids:
            speakers_uuids.remove(SPEAKER_NARRATOR)
            speakers_uuids.append('NARRATOR')
        loca_dict = dict[str, str]()
        xml_file = None
        try:
            loca_file = self.__assets.tool.unpack('Localization/English', 'Localization/English/english.loca')
            xml_file = self.__assets.tool.convert_loca_to_xml(loca_file)
        except:
            loca_file = None
        if loca_file is None:
            xml_file = self.__assets.tool.unpack('Localization/English', 'Localization/English/english.xml')
        if xml_file is None:
            raise RuntimeError('Failed to find english.loca or english.xml')
        xml = et.parse(xml_file)
        for element in xml.getroot():
            if isinstance(element, et.Element):
                text_handle = element.attrib['contentuid']
                text_content = element.text
                if text_handle is not None and text_content is not None:
                    loca_dict[text_handle] = text_content

        os.makedirs(os.path.join(os.getcwd(), "__scanner__", "dialog_index"), exist_ok=True)
        text_handles = dict[str, frozenset]()
        filepaths = dict[str, str]()
        for speaker_uuid in speakers_uuids:
            soundbank_name = speaker_uuid.replace('-', '')

            try:
                sb = soundbank_object(game_file(self.__assets.tool, f'Mods/Gustav/Localization/English/Soundbanks/{soundbank_name}.lsf', pak_name='Localization/VoiceMeta'))
            except:
                sb = None
            if sb is None:
                try:
                    sb = soundbank_object(game_file(self.__assets.tool, f'Mods/Gustav/Localization/English/Soundbanks/{soundbank_name}.lsf', pak_name='Localization/Voice'))
                except Exception as ex:
                    sb = None
            if sb is None:
                try:
                    sb = soundbank_object(game_file(self.__assets.tool, f'Localization/English/Soundbanks/{soundbank_name}.lsf', pak_name='Localization/Voice'))
                except Exception as ex:
                    sb = None
                
            if sb is not None:
                text_handles[speaker_uuid] = frozenset(sb.get_all_text_handles())
                sb = None        
                filepath = os.path.join(os.getcwd(), "__scanner__", "dialog_index", speaker_uuid + ".json")
                if os.path.isfile(filepath):
                    os.unlink(filepath)
                with open(filepath, "at") as fd:
                    fd.write("[\n")
                filepaths[speaker_uuid] = filepath
                filepath = None
                self.__line_count[speaker_uuid] = 0
            else:
                print(f'Soundbank of a speaker {speaker_uuid} is not found')

        def process_dialog(dialog: dialog_object) -> None:
            for speaker_uuid in speakers_uuids:
                if speaker_uuid not in text_handles:
                    continue
                dialog_tagged_texts = dialog.get_all_tagged_texts()
                ths = text_handles[speaker_uuid].intersection(dialog_tagged_texts.keys())
                if len(ths) > 0:
                    result = dict[str, str]()
                    filename = os.path.basename(dialog.filename).replace('\\', '-')
                    for th in ths:
                        version = dialog_tagged_texts[th]
                        if th in loca_dict:
                            text = loca_dict[th]
                            result[th + ' / ' + str(version)] = text
                    if len(result) > 0:
                        c = self.__line_count[speaker_uuid]
                        self.__line_count[speaker_uuid]  = c + len(result)
                        with open(filepaths[speaker_uuid], "at") as fd:
                            fd.write('  {\n    "filename": "' + filename + '"')
                            for k, v in result.items():
                                if k == 'filename':
                                    continue
                                fd.write(f',\n    "{k}": "{v}"')
                            fd.write("\n  },\n")

        self.scan_dialogs(process_dialog, early_access=early_access)
        for speaker_uuid in speakers_uuids:
            if speaker_uuid not in text_handles:
                continue
            with open(filepaths[speaker_uuid], "at") as fd:
                fd.write('  {\n    "filename": ""\n  }\n]\n')
        line_count_filepath = os.path.join(os.getcwd(), "__scanner__", "dialog_index", "line_count.json")
        with open(line_count_filepath, 'wt') as f:
            json.dump(self.__line_count, f, sort_keys = True, indent = 4)


