from __future__ import annotations

import decimal as dc
import xml.etree.ElementTree as et

from ._assets import bg3_assets
from ._common import quaternion_to_euler
from ._scene import scene_object
from ._timeline import timeline_object

# DOFAperature
# DOFFarSharpDistance
# DOFNearSharpDistance
# DOFFocalDistance
# DampingStrength

class scene_camera_tool:
    __assets: bg3_assets
    __scenes: tuple[scene_object, ...]
    __loaded_scenes: set[str]
    __timeline: timeline_object

    @property
    def scenes(self) -> tuple[scene_object, ...]:
        return self.__scenes

    def __init__(self, a: bg3_assets, dialog_name: str) -> None:
        self.__assets = a
        self.__timeline = self.__assets.get_timeline_object(dialog_name)
        self.__loaded_scenes = set[str]()
        scenes_load_order = list[scene_object]()
        s = self.__assets.get_scene_object(dialog_name)
        self.__load_inherited_scenes(s, scenes_load_order)
        self.__scenes = tuple(reversed(scenes_load_order))

    def __load_scene(self, scene_file: str) -> scene_object:
        pak = self.__assets.index.get_pak_by_file(scene_file)
        lsf_file = self.__assets.files.get_file(pak, scene_file, exclude_from_build = True)
        return scene_object(lsf_file)

    def __load_inherited_scenes(self, s: scene_object, scenes_load_order: list[scene_object]) -> None:
        scenes_load_order.append(s)
        inherited_scenes = s.get_inherited_scenes()
        new_scenes = list[scene_object]()
        for scene_file in inherited_scenes:
            if scene_file in self.__loaded_scenes:
                continue
            scene = self.__load_scene(scene_file)
            new_scenes.append(scene)
            self.__loaded_scenes.add(scene_file)
        for scene in new_scenes:
            self.__load_inherited_scenes(scene, scenes_load_order)

    def get_camera_transform(self, camera_uuid: str, stage_uuid: str) -> tuple[tuple[str, str, str], tuple[str, str, str], str] | None:
        if self.__timeline.is_camera_container(camera_uuid):
            camera_uuid = self.__timeline.get_camera_from_container(camera_uuid)
        result_transform = None
        for s in self.__scenes:
            try:
                transform = s.get_camera_transform(camera_uuid, stage_uuid)
            except:
                transform = None
            if transform is None and result_transform is None:
                try:
                    transform = s.get_camera_transform(camera_uuid)
                except:
                    transform = None
            if transform is not None:
                result_transform = transform
        if result_transform is None:
            return None
        x, y, z, w = result_transform[1]
        a, b, c = quaternion_to_euler(float(x), float(y), float(z), float(w), sequence = 'yxz')
        return (result_transform[0], (str(a), str(b), str(c)), result_transform[2])
