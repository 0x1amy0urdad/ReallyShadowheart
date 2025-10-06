from __future__ import annotations

import datetime
import functools
import os.path
import shutil
import sys
import traceback

import bg3moddinglib as bg3

from .context import files, ea_files, ea_tool


def copy_facefx_data(speaker_id: str) -> None:
    unpacked_ffxactor = ea_tool.unpack(
        'Localization/English_Animations',
        f'Localization/English/Animation/FaceFXActors/{speaker_id}.ffxactor')
    unpacked_ffxbones = ea_tool.unpack(
        'Localization/English_Animations',
        f'Localization/English/Animation/FaceFXActors/{speaker_id}.ffxbones')
    dest_dir_path = files.mod_destination_dir_path('Mods/ModNameHere/Localization/English/Animation/FaceFXActors')
    os.makedirs(dest_dir_path, exist_ok = True)
    shutil.copy(unpacked_ffxactor, dest_dir_path)
    shutil.copy(unpacked_ffxbones, dest_dir_path)

def copy_voice_data(speaker_id: str) -> None:
    log_path = os.path.join(files.tool.env.env_root_path, 'really_shadowheart_extension.log')
    with open(log_path, 'wt', encoding='utf-8', errors='replace') as f:
        bg3.print_and_write(f, '\n')
        try:
            soundbank = bg3.soundbank_object.create_new(files, speaker_id)
            textbank = bg3.loca_object(files.add_new_file(files.get_loca_relative_path()))

            full_game_sb = bg3.soundbank_object(
                files.get_file(
                    'Localization/VoiceMeta',
                    f'Mods/Gustav/Localization/English/Soundbanks/{soundbank.soundbank_id}.lsf',
                    exclude_from_build = True))
            ea_sb = bg3.soundbank_object(
                ea_files.get_file(
                    'Localization/Voice',
                    f'Localization/English/Soundbanks/{soundbank.soundbank_id}.lsf',
                    exclude_from_build = True))

            full_game_voice_lines = frozenset(full_game_sb.get_all_text_handles())
            ea_voice_lines = frozenset(ea_sb.get_all_text_handles())

            ea_textbank = bg3.loca_object(ea_files.get_text_bank_file())

            cut_voice_lines = ea_voice_lines - full_game_voice_lines

            wem_dir_path = files.mod_destination_dir_path(os.path.dirname(soundbank.file.relative_file_path))
            os.makedirs(wem_dir_path, exist_ok = True)
            bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} wem_dir_path = {wem_dir_path}')

            anim_dir_path = files.mod_destination_dir_path(os.path.dirname(soundbank.file.relative_file_path.replace('Soundbanks', 'Animation')))
            os.makedirs(anim_dir_path, exist_ok = True)
            bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} anim_dir_path = {anim_dir_path}')
        
            cache_dir_path = os.path.join(files.tool.env.env_root_path, 'cache')
            os.makedirs(cache_dir_path, exist_ok = True)
            bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} cache_dir_path = {cache_dir_path}')
        
        except BaseException as ex:
            t, v, tb = sys.exc_info()
            bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} failed due to exception')
            bg3.print_and_write(f, traceback.format_exception(t, v, tb))
            raise ex

        processed = 0
        total = len(cut_voice_lines)
        for voice_line_handle in cut_voice_lines:
            wem_file_name = ea_sb.get_wem_file_name(voice_line_handle)
            processed += 1
            if not wem_file_name.endswith('.wem'):
                bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} [{processed}/{total}] skipped {voice_line_handle}, no .wem file')
                continue

            base_file_name = wem_file_name[:-4] 
            ffxanim_file_name = f'Localization/English/Animation/FX_{base_file_name}.ffxanim'
            gr2_file_name = f'Localization/English/Animation/MC_{base_file_name}.gr2'
            wem_file_name = f'Localization/English/Soundbanks/{base_file_name}.wem'
            text_handle = base_file_name.split('_')[1]
            unpacked_ffxanim_file = ''
            unpacked_gr2_file = ''
            unpacked_wem_file = ''

            cached_ffxanim_file = os.path.join(cache_dir_path, f'FX_{base_file_name}.ffxanim')
            cached_gr2_file = os.path.join(cache_dir_path, f'MC_{base_file_name}.gr2')
            cached_wem_file = os.path.join(cache_dir_path, f'{base_file_name}.wem')
        
            if os.path.isfile(cached_wem_file) and os.path.isfile(cached_ffxanim_file):
                unpacked_ffxanim_file = cached_ffxanim_file
                unpacked_wem_file = cached_wem_file
                if os.path.isfile(cached_gr2_file):
                    unpacked_gr2_file = cached_gr2_file
            else:
                try:
                    unpacked_ffxanim_file = ea_tool.unpack('Localization/English_Animations.pak', ffxanim_file_name)
                    shutil.copy(unpacked_ffxanim_file, cache_dir_path)
                except:
                    bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} unpacking {voice_line_handle}, missing ffxanim file {ffxanim_file_name}')
                try:
                    unpacked_gr2_file = ea_tool.unpack('Localization/English_Animations.pak', gr2_file_name)
                    shutil.copy(unpacked_gr2_file, cache_dir_path)
                except:
                    bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} unpacking {voice_line_handle}, missing gr2 file {gr2_file_name}')
                try:
                    unpacked_wem_file = ea_tool.unpack('Localization/Voice.pak', wem_file_name)
                    shutil.copy(unpacked_wem_file, cache_dir_path)
                except:
                    bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} unpacking {voice_line_handle}, missing wem file {wem_file_name}')

            if not unpacked_ffxanim_file or not unpacked_wem_file:
                bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} [{processed}/{total}] skipped {voice_line_handle} due to missing files')
                continue
            try:
                text = ea_textbank.get_line(voice_line_handle)
                duration = ea_sb.get_duration(voice_line_handle)
            except:
                bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} [{processed}/{total}] skipped {voice_line_handle}, handle {voice_line_handle} is not found in the ea soundbank')
                continue

            try:
                textbank.add_line(text_handle, 1, text)
            except:
                bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} text_handle = {text_handle}, text = {text}')
            soundbank.add_voice_metadata(text_handle, duration, base_file_name + '.wem')

            shutil.copy(unpacked_ffxanim_file, anim_dir_path)
            if unpacked_gr2_file:
                shutil.copy(unpacked_gr2_file, anim_dir_path)
            shutil.copy(unpacked_wem_file, wem_dir_path)

            bg3.print_and_write(f, f'{datetime.datetime.now().astimezone()} [{processed}/{total}] finished unpacking {voice_line_handle}')


def fix_text_content() -> None:
    loca = bg3.loca_object(files.add_new_file(files.get_loca_relative_path()))
    try:
        loca.update_line('hb29103d5gb3e9g4917ga0bagda2d1225c7d2', 2, "Quite harsh of you. I can't say I entirely disagree, but still... quite harsh.")
    except:
        pass


bg3.add_build_procedure('copy_facefx_data', functools.partial(copy_facefx_data, bg3.SPEAKER_SHADOWHEART))
bg3.add_build_procedure('copy_voice_data', functools.partial(copy_voice_data, bg3.SPEAKER_SHADOWHEART))
bg3.add_build_procedure('fix_text_content', fix_text_content)
