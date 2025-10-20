from __future__ import annotations

import xml.etree.ElementTree as et

from ._common import (
    get_bg3_attribute,
    get_or_create_child_node,
    get_required_bg3_attribute,
    set_bg3_attribute,
    new_random_uuid,
    to_compact_string,
    put_object_into_map,
    find_object_by_map_key
)
from ._files import game_file

from typing import Iterable

class scene_object:
    DEFAULT_STAGE_UUID: str = '00000000-0000-0000-0000-000000000000'

    __lsf_file: game_file
    __lsx_file: game_file
    __current_stage_uuid: str | None

    def __init__(self, lsf_file: game_file, lsx_file: game_file) -> None:
        self.__lsf_file = lsf_file
        self.__lsx_file = lsx_file
        self.__current_stage_uuid = None

    @property
    def current_stage_uuid(self) -> str:
        if self.__current_stage_uuid is None:
            raise ValueError('no stage has been created yet')
        return self.__current_stage_uuid

    @property
    def lsf_xml(self) -> et.Element:
        return self.__lsf_file.root_node

    @property
    def lsx_xml(self) -> et.Element:
        return self.__lsx_file.root_node

    def get_actor_type(self, index: int) -> int:
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor_type = get_bg3_attribute(actors[index], 'ActorType')
        if isinstance(actor_type, str):
            return int(actor_type)
        return 0

    def get_number_of_actors(self) -> int:
        return len(self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]'))

    def get_actor_position(self, index: int) -> tuple[str, str, str]:
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine position of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        position = get_required_bg3_attribute(transform, 'Position')
        positions = position.split(' ')
        if len(positions) != 3:
            raise RuntimeError(f'Unexpected number ({len(positions)}) of components in position, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        return (positions[0], positions[1], positions[2])

    def set_actor_position(self, index: int, pos: tuple[str | float, str | float, str | float]) -> None:
        # update lsf
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine position of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'Position', f'{pos[0]} {pos[1]} {pos[2]}', attribute_type = 'fvec3')

        # update lsx
        actors = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsx_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of an actor with index {index} in {self.__lsx_file.relative_file_path}')
        attr = transform.find('./attribute[@id="Position"]')
        if attr is not None:
            transform.remove(attr)
        transform.append(et.fromstring(f'<attribute id="Position" type="fvec3"><float3 x="{pos[0]}" y="{pos[1]}" z="{pos[2]}" /></attribute>'))

    def get_actor_rotation(self, index: int) -> tuple[str, str, str, str]:
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine rotation of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        rotation = get_required_bg3_attribute(transform, 'RotationQuat')
        rotations = rotation.split(' ')
        if len(rotations) != 4:
            raise RuntimeError(f'Unexpected number ({len(rotations)}) of components in rotation, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        return (rotations[0], rotations[1], rotations[2], rotations[3])

    def set_actor_rotation(self, index: int, rot: tuple[str | float, str | float, str | float, str | float]) -> None:
        # update lsf
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine rotation of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'RotationQuat', f'{rot[0]} {rot[1]} {rot[2]} {rot[3]}', attribute_type = 'fvec4')

        # update lsx
        actors = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsx_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of an actor with index {index} in {self.__lsx_file.relative_file_path}')
        attr = transform.find('./attribute[@id="RotationQuat"]')
        if attr is not None:
            transform.remove(attr)
        transform.append(et.fromstring(f'<attribute id="RotationQuat" type="fvec4"><float3 x="{rot[0]}" y="{rot[1]}" z="{rot[2]}" w="{rot[3]}" /></attribute>'))

    def get_actor_scale(self, index: int) -> str:
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine scale of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        return get_required_bg3_attribute(transform, 'Scale')

    def set_actor_scale(self, index: int, scale: str) -> None:
        # update lsf
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine rotation of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'Scale', f'{scale}', attribute_type = 'float')

        # update lsx
        actors = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsx_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of an actor with index {index} in {self.__lsx_file.relative_file_path}')
        set_bg3_attribute(transform, 'Scale', f'{scale}', attribute_type = 'float')

    def get_actor_transform(self, index: int) -> tuple[tuple[str, str, str], tuple[str, str, str, str], str]:
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        position = get_required_bg3_attribute(transform, 'Position')
        positions = position.split(' ')
        if len(positions) != 3:
            raise RuntimeError(f'Unexpected number ({len(positions)}) of components in position, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        rotation = get_required_bg3_attribute(transform, 'RotationQuat')
        rotations = rotation.split(' ')
        if len(rotations) != 4:
            raise RuntimeError(f'Unexpected number ({len(rotations)}) of components in rotation, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        scale = get_required_bg3_attribute(transform, 'Scale')
        return ((positions[0], positions[1], positions[2]), (rotations[0], rotations[1], rotations[2], rotations[3]), scale)

    def set_actor_transform(self, index: int, pos: tuple[str, str, str], rot: tuple[str, str, str, str], scale: str) -> None:
        # update lsf
        actors = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsf_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of an actor with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'Position', f'{pos[0]} {pos[1]} {pos[2]}', attribute_type = 'fvec3')
        set_bg3_attribute(transform, 'RotationQuat', f'{rot[0]} {rot[1]} {rot[2]} {rot[3]}', attribute_type = 'fvec4')
        set_bg3_attribute(transform, 'Scale', f'{scale}', attribute_type = 'float')

        # update lsx
        actors = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        if index >= len(actors):
            raise KeyError(f'There is no actor with index {index} in {self.__lsx_file.relative_file_path}')
        actor = actors[index]
        transform = actor.find('./children/node[@id="Transforms"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of an actor with index {index} in {self.__lsx_file.relative_file_path}')
        all_attrs = transform.findall('./attribute')
        for attr in all_attrs:
            transform.remove(attr)
        transform.append(et.fromstring(f'<attribute id="Position" type="fvec3"><float3 x="{pos[0]}" y="{pos[1]}" z="{pos[2]}" /></attribute>'))
        transform.append(et.fromstring(f'<attribute id="RotationQuat" type="fvec4"><float3 x="{rot[0]}" y="{rot[1]}" z="{rot[2]}" w="{rot[3]}" /></attribute>'))
        transform.append(et.fromstring(f'<attribute id="Scale" type="float" value="{scale}" />'))

    def is_attached_camera(self, index: int) -> bool:
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        return get_bg3_attribute(camera, 'AttachTo') is not None

    def get_number_of_cameras(self) -> int:
        return len(self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]'))

    def get_camera_position(self, index: int) -> tuple[str, str, str]:
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        position = get_required_bg3_attribute(transform, 'Position')
        positions = position.split(' ')
        if len(positions) != 3:
            raise RuntimeError(f'Unexpected number ({len(positions)}) of components in position, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        return (positions[0], positions[1], positions[2])

    def set_camera_position(self, index: int, pos: tuple[str, str, str]) -> None:
        # update lsf
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'Position', f'{pos[0]} {pos[1]} {pos[2]}', attribute_type = 'fvec3')

        # update lsx
        cameras = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        attr = transform.find('./attribute[@id="Position"]')
        if attr is not None:
            transform.remove(attr)
        transform.append(et.fromstring(f'<attribute id="Position" type="fvec3"><float3 x="{pos[0]}" y="{pos[1]}" z="{pos[2]}" /></attribute>'))

    def get_camera_rotation(self, index: int) -> tuple[str, str, str, str]:
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        rotation = get_required_bg3_attribute(transform, 'RotationQuat')
        rotations = rotation.split(' ')
        if len(rotations) != 4:
            raise RuntimeError(f'Unexpected number ({len(rotations)}) of components in rotation, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        return (rotations[0], rotations[1], rotations[2], rotations[3])

    def set_camera_rotation(self, index: int, rot: tuple[str, str, str, str]) -> None:
        # update lsf
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'RotationQuat', f'{rot[0]} {rot[1]} {rot[2]} {rot[3]}', attribute_type = 'fvec4')

        # update lsx
        cameras = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        attr = transform.find('./attribute[@id="RotationQuat"]')
        if attr is not None:
            transform.remove(attr)
        transform.append(et.fromstring(f'<attribute id="RotationQuat" type="fvec4"><float3 x="{rot[0]}" y="{rot[1]}" z="{rot[2]}" w="{rot[3]}" /></attribute>'))

    def get_camera_scale(self, index: int) -> str:
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        return get_required_bg3_attribute(transform, 'Scale')

    def set_camera_scale(self, index: int, scale: str) -> None:
        # update lsf
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'Scale', f'{scale}', attribute_type = 'float')

        # update lsx
        cameras = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'Scale', f'{scale}', attribute_type = 'float')

    def get_camera_transform(self, index: int) -> tuple[tuple[str, str, str], tuple[str, str, str, str], str]:
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        position = get_required_bg3_attribute(transform, 'Position')
        positions = position.split(' ')
        if len(positions) != 3:
            raise RuntimeError(f'Unexpected number ({len(positions)}) of components in position, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        rotation = get_required_bg3_attribute(transform, 'RotationQuat')
        rotations = rotation.split(' ')
        if len(rotations) != 4:
            raise RuntimeError(f'Unexpected number ({len(rotations)}) of components in rotation, actor index {index}, scene file {self.__lsf_file.relative_file_path}')
        scale = get_required_bg3_attribute(transform, 'Scale')
        return ((positions[0], positions[1], positions[2]), (rotations[0], rotations[1], rotations[2], rotations[3]), scale)

    def set_camera_transform(self, index: int, pos: tuple[str, str, str], rot: tuple[str, str, str, str], scale: str) -> None:
        # update lsf
        cameras = self.lsf_xml.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        set_bg3_attribute(transform, 'Position', f'{pos[0]} {pos[1]} {pos[2]}', attribute_type = 'fvec3')
        set_bg3_attribute(transform, 'RotationQuat', f'{rot[0]} {rot[1]} {rot[2]} {rot[3]}', attribute_type = 'fvec4')
        set_bg3_attribute(transform, 'Scale', f'{scale}', attribute_type = 'float')

        # update lsx
        cameras = self.lsx_xml.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]/children/node[@id="Object"]')
        if index >= len(cameras):
            raise KeyError(f'There is no camera with index {index} in {self.__lsf_file.relative_file_path}')
        camera = cameras[index].find('./children/node[@id="TLCameras"]')
        if camera is None:
            raise KeyError(f'Failed to find a camera with index {index} in {self.__lsf_file.relative_file_path}')
        transform = camera.find('./children/node[@id="Transform"]/children/node[@id="Object"]/children/node[@id="MapValue"]')
        if transform is None:
            raise RuntimeError(f'Failed to determine transform of a camera with index {index} in {self.__lsf_file.relative_file_path}')
        all_attrs = transform.findall('./attribute')
        for attr in all_attrs:
            transform.remove(attr)
        transform.append(et.fromstring(f'<attribute id="Position" type="fvec3"><float3 x="{pos[0]}" y="{pos[1]}" z="{pos[2]}" /></attribute>'))
        transform.append(et.fromstring(f'<attribute id="RotationQuat" type="fvec4"><float3 x="{rot[0]}" y="{rot[1]}" z="{rot[2]}" w="{rot[3]}" /></attribute>'))
        transform.append(et.fromstring(f'<attribute id="Scale" type="float" value="{scale}" />'))

    def set_light_radius(
            self,
            light_id: str,
            radius: float | str,
            /,
            lighting_setup_id: str = '00000000-0000-0000-0000-000000000000'
    ) -> None:
        lsf_lights = self.__get_lights_lsf(lighting_setup_id)
        if light_id not in lsf_lights:
            raise RuntimeError(f'Light {light_id} is not found in lighting setup f{lighting_setup_id} in f{self.__lsf_file.relative_file_path}')
        set_bg3_attribute(lsf_lights[light_id], 'Radius', str(radius), attribute_type = 'float')

        lsx_lights = self.__get_lights_lsx(lighting_setup_id)
        if light_id not in lsx_lights:
            raise RuntimeError(f'Light {light_id} is not found in lighting setup f{lighting_setup_id} in f{self.__lsx_file.relative_file_path}')
        set_bg3_attribute(lsx_lights[light_id], 'Radius', str(radius), attribute_type = 'float')


    def set_light_position(
            self,
            light_id: str,
            pos: tuple[float | str, float | str, float | str],
            /,
            lighting_setup_id: str = '00000000-0000-0000-0000-000000000000'
    ) -> None:
        lsf_lights = self.__get_lights_lsf(lighting_setup_id)
        if light_id not in lsf_lights:
            raise RuntimeError(f'Light {light_id} is not found in lighting setup f{lighting_setup_id} in f{self.__lsf_file.relative_file_path}')
        set_bg3_attribute(lsf_lights[light_id], 'Position', f'{pos[0]} {pos[1]} {pos[2]}', attribute_type = 'fvec3')

        lsx_lights = self.__get_lights_lsx(lighting_setup_id)
        if light_id not in lsx_lights:
            raise RuntimeError(f'Light {light_id} is not found in lighting setup f{lighting_setup_id} in f{self.__lsx_file.relative_file_path}')
        pos_attr = lsx_lights[light_id].find('./attribute[@id="Position"]/float3')
        if pos_attr is None:
            raise RuntimeError(f'Light {light_id} does not have a position')
        pos_attr.set('x', str(pos[0]))
        pos_attr.set('y', str(pos[1]))
        pos_attr.set('z', str(pos[2]))


    def __get_lights_lsf(self, lighting_setup_id: str) -> dict[str, et.Element]:
        root_node = self.__lsf_file.xml.getroot()
        setups = root_node.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="LightingSetups"]/children/node[@id="LightingSetup"]')
        for setup in setups:
            setup_id = get_required_bg3_attribute(setup, 'Id')
            if setup_id == lighting_setup_id:
                lights = setup.findall('./children/node[@id="Lights"]/children/node[@id="Light"]')
                return { get_required_bg3_attribute(light, 'Id') : light for light in lights }
        raise RuntimeError(f'Lighting setup {lighting_setup_id} not found in {self.__lsf_file}')

    def __get_lights_lsx(self, lighting_setup_id: str) -> dict[str, et.Element]:
        root_node = self.__lsx_file.xml.getroot()
        setups = root_node.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="LightingSetups"]/children/node[@id="LightingSetup"]')
        for setup in setups:
            setup_id = get_required_bg3_attribute(setup, 'Id')
            if setup_id == lighting_setup_id:
                lights = setup.findall('./children/node[@id="Lights"]/children/node[@id="Light"]')
                return { get_required_bg3_attribute(light, 'Id') : light for light in lights }
        raise RuntimeError(f'Lighting setup {lighting_setup_id} not found in {self.__lsf_file}')

    def set_direction_light_dims(
            self,
            light_uuid: str,
            stage_uuid: str,
            dimensions: tuple[float, float, float]
    ) -> None:
        light = self.__get_light_element_lsf(light_uuid)
        desc = light.find('./children/node[@id="Desc"]')
        if desc is None:
            raise RuntimeError(f'Light without a Desc node: {light_uuid} in {self.__lsf_file.relative_file_path}')
        dld = get_or_create_child_node(desc, 'DirectionLightDimensions')
        obj = et.fromstring(''.join([
            '<node id="Object">',
            f'<attribute id="MapKey" type="guid" value="{stage_uuid}" />',
            f'<attribute id="MapValue" type="fvec3" value="{dimensions[0]} {dimensions[1]} {dimensions[2]}" />',
            '</node>']))
        put_object_into_map(dld, obj)

        light = self.__get_light_element_lsx(light_uuid)
        desc = light.find('./children/node[@id="Desc"]')
        if desc is None:
            raise RuntimeError(f'Light without a Desc node: {light_uuid} in {self.__lsx_file.relative_file_path}')
        dld = get_or_create_child_node(desc, 'DirectionLightDimensions')
        obj = et.fromstring(''.join([
            '<node id="Object">',
            f'<attribute id="MapKey" type="guid" value="{stage_uuid}" />',
            f'<attribute id="MapValue" type="fvec3">',
            f'<float3 x="{dimensions[0]}" y="{dimensions[1]}" z="{dimensions[2]}" />',
            '</attribute></node>']))
        put_object_into_map(dld, obj)


    def __get_light_element_lsf(self, light_uuid: str) -> et.Element:
        root_node = self.__lsf_file.xml.getroot()
        lights = root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="Lights"]')
        if lights is None:
            raise RuntimeError(f'No lights defined in scene {self.__lsf_file.relative_file_path}')
        light = find_object_by_map_key(lights, light_uuid)
        if light is None:
            raise RuntimeError(f'No light {light_uuid} defined in scene {self.__lsf_file.relative_file_path}')
        result = light.find('./children/node[@id="Lights"]')
        if result is None:
            raise RuntimeError(f'Corrupted scene file: {self.__lsf_file.relative_file_path}')
        return result

    def __get_light_element_lsx(self, light_uuid: str) -> et.Element:
        root_node = self.__lsx_file.xml.getroot()
        lights = root_node.find('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="Lights"]')
        if lights is None:
            raise RuntimeError(f'No lights defined in scene {self.__lsf_file.relative_file_path}')
        light = find_object_by_map_key(lights, light_uuid)
        if light is None:
            raise RuntimeError(f'No light {light_uuid} defined in scene {self.__lsf_file.relative_file_path}')
        result = light.find('./children/node[@id="Lights"]')
        if result is None:
            raise RuntimeError(f'Corrupted scene file: {self.__lsf_file.relative_file_path}')
        return result


    def create_new_actor(
            self,
            templaye_uuid: str,
            actor_type: int,
            look_at_mode: int,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            important_for_staging: bool = True,
            is_terrain_snapping_in_game_disabled = True
    ) -> None:
        default_stage_uuid = '00000000-0000-0000-0000-000000000000'
        actor_node = et.fromstring("".join([
            '<node id="TLActor">',
            f'<attribute id="ActorType" type="uint8" value="{actor_type}" />',
            f'<attribute id="LookAtMode" type="uint8" value="{look_at_mode}" />',
            f'<attribute id="TemplateId" type="guid" value="{templaye_uuid}" />',
            '<attribute id="ImportantForStaging" type="bool" value="True" />' if important_for_staging else '',
            '<attribute id="IsTerrainSnappingInGameDisabled" type="bool" value="True" />' if is_terrain_snapping_in_game_disabled else '',
            '<children><node id="Transforms"><children>',
            f'<node id="Object"><attribute id="MapKey" type="guid" value="{default_stage_uuid}"/><children></children></node>',
            '</children></node></children></node>'
        ]))

        root_node = self.__lsf_file.xml.getroot()
        actors = root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children')
        if actors is None:
            raise RuntimeError(f'Could not add a new actor to {self.__lsf_file.relative_file_path}')
        actors.append(actor_node)

        root_node = self.__lsx_file.xml.getroot()
        actors = root_node.find('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLActors"]/children')
        if actors is None:
            raise RuntimeError(f'Could not add a new actor to {self.__lsx_file.relative_file_path}')
        actors.append(actor_node)

        self.set_actor_transform_to_stage(templaye_uuid, position, rotation, scale, stage_uuid = default_stage_uuid)


    def create_new_stage(self, /, stage_uuid: str | None = None, name: str | None = None) -> str:
        if stage_uuid is None:
            stage_uuid = new_random_uuid()
        if name is None:
            name = "Unnamed stage"
        self.__current_stage_uuid = stage_uuid

        new_stage = et.fromstring(''.join([
            '<node id="TLStage">',
            f'<attribute id="Identifier" type="guid" value="{self.__current_stage_uuid}" />',
            f'<attribute id="Name" type="LSString" value="{name}" />',
            '</node>'
        ]))

        root_node = self.__lsf_file.xml.getroot()
        scene_children = root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]/children')
        if not isinstance(scene_children, et.Element):
            raise ValueError(f"{self.__lsf_file.relative_file_path} is not a valid scene")
        stages = scene_children.find('./node[@id="TLStages"]')
        if not isinstance(stages, et.Element):
            stages = et.fromstring('<node id="TLStages"><children></children></node>')
            scene_children.append(stages)
        stages_children = stages.find('./children')
        if not isinstance(stages_children, et.Element):
            stages_children = et.fromstring('<children></children>')
            stages.append(stages_children)
        stages_children.append(new_stage)

        root_node = self.__lsx_file.xml.getroot()
        scene_children = root_node.find('./region[@id="TLScene"]/node[@id="root"]/children')
        if not isinstance(scene_children, et.Element):
            raise ValueError(f"{self.__lsx_file.relative_file_path} is not a valid scene")
        stages = scene_children.find('./node[@id="TLStages"]')
        if not isinstance(stages, et.Element):
            stages = et.fromstring('<node id="TLStages"><children></children></node>')
            scene_children.append(stages)
        stages_children = stages.find('./children')
        if not isinstance(stages_children, et.Element):
            stages_children = et.fromstring('<children></children>')
            stages.append(stages_children)
        stages_children.append(new_stage)

        return stage_uuid

    def set_actor_transform_to_stage(
            self,
            template_uuid: str,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        root_node = self.__lsf_file.xml.getroot()
        actors = root_node.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        found = False
        for actor in actors:
            tpl_uuid = get_bg3_attribute(actor, 'TemplateId')
            if isinstance(tpl_uuid, str) and tpl_uuid == template_uuid:
                self.__put_transform_into_stage_lsf(actor, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find actor {template_uuid} in {self.__lsf_file.relative_file_path}')

        found = False
        root_node = self.__lsx_file.xml.getroot()
        actors = root_node.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLActors"]/children/node[@id="TLActor"]')
        for actor in actors:
            tpl_uuid = get_bg3_attribute(actor, 'TemplateId')
            if isinstance(tpl_uuid, str) and tpl_uuid == template_uuid:
                self.__put_transform_into_stage_lsx(actor, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find actor {template_uuid} in {self.__lsx_file.relative_file_path}')

    def set_camera_transform_in_stage(
            self,
            camera_uuid: str,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        found = False
        root_node = self.__lsf_file.xml.getroot()
        cameras = root_node.findall('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]/children/node[@id="Object"]/children/node[@id="TLCameras"]')
        for camera in cameras:
            identifier = get_required_bg3_attribute(camera, 'Identifier')
            if identifier == camera_uuid:
                self.__put_transform_into_stage_lsf(camera, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find camera {camera_uuid} in {self.__lsf_file.relative_file_path}')

        found = False
        root_node = self.__lsx_file.xml.getroot()
        cameras = root_node.findall('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]/children/node[@id="Object"]/children/node[@id="TLCameras"]')
        for camera in cameras:
            identifier = get_required_bg3_attribute(camera, 'Identifier')
            if identifier == camera_uuid:
                self.__put_transform_into_stage_lsx(camera, position, rotation, scale, stage_uuid = stage_uuid)
                found = True
                break
        if not found:
            raise ValueError(f'cannot find camera {camera_uuid} in {self.__lsf_file.relative_file_path}')

    def add_lights_to_camera(self, camera_uuid: str, lights_uuids: Iterable[str], /, stage_uuid: str | None = None) -> None:
        if stage_uuid is None:
            stage_uuid = self.__current_stage_uuid
        if stage_uuid is None:
            raise ValueError("can't add lights, either create a new stage or pass stage uuid to this call")

        lights_uuids = set(lights_uuids)

        new_lights = list[et.Element]()
        for light_uuid in lights_uuids:
            new_lights.append(et.fromstring(f'<node id="MapValue"><attribute id="Object" type="guid" value="{light_uuid}"/></node>'))
        root_node = self.__lsf_file.xml.getroot()
        cameras = root_node.find('./region[@id="TLScene"]/node[@id="TLScene"]/children/node[@id="TLCameras"]')
        if not isinstance(cameras, et.Element):
            raise RuntimeError(f'bad stage file {self.__lsf_file.relative_file_path}')
        camera = find_object_by_map_key(cameras, camera_uuid)
        if camera is None:
            raise KeyError(f'camera {camera_uuid} is not found in {self.__lsf_file.relative_file_path}')
        lights = camera.findall('./children/node[@id="TLCameras"]/children/node[@id="LinkedLights"]')
        self.__add_lights(lights, new_lights, lights_uuids, stage_uuid)

        new_lights = list[et.Element]()
        for light_uuid in lights_uuids:
            new_lights.append(et.fromstring(f'<node id="MapValue"><attribute id="Object" type="guid" value="{light_uuid}"/></node>'))
        root_node = self.__lsx_file.xml.getroot()
        cameras = root_node.find('./region[@id="TLScene"]/node[@id="root"]/children/node[@id="TLCameras"]')
        if not isinstance(cameras, et.Element):
            raise RuntimeError(f'bad stage file {self.__lsx_file.relative_file_path}')
        camera = find_object_by_map_key(cameras, camera_uuid)
        if camera is None:
            raise KeyError(f'camera {camera_uuid} is not found in {self.__lsx_file.relative_file_path}')
        lights = camera.findall('./children/node[@id="TLCameras"]/children/node[@id="LinkedLights"]')
        self.__add_lights(lights, new_lights, lights_uuids, stage_uuid)

    def __add_lights(self, lights: Iterable[et.Element], new_lights: Iterable[et.Element], lights_uuids: set[str], stage_uuid: str) -> None:
        for light in lights:
            stage_lights = find_object_by_map_key(light, stage_uuid)
            if stage_lights is not None:
                children = stage_lights.find('./children')
                if children is None:
                    children = et.fromstring('<children></children>')
                    for light in new_lights:
                        children.append(light)
                    stage_lights.append(children)
                else:
                    existing_lights = children.findall('./node[@id="Object"]')
                    for existing_light in existing_lights:
                        light_uuid = get_required_bg3_attribute(existing_light, 'Object')
                        if light_uuid in lights_uuids:
                            raise ValueError(f"duplicate light: {light_uuid}")
                    for light in new_lights:
                        children.append(light)

    def __put_transform_into_stage_lsf(
            self,
            target: et.Element,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        if stage_uuid is None:
            stage_uuid = self.__current_stage_uuid
        new_transform = et.fromstring(''.join([
                '<node id="Object">',
                f'<attribute id="MapKey" type="guid" value="{stage_uuid}" />',
                '<children><node id="MapValue">',
                f'<attribute id="Position" type="fvec3" value="{position[0]} {position[1]} {position[2]}" />',
                f'<attribute id="RotationQuat" type="fvec4" value="{rotation[0]} {rotation[1]} {rotation[2]} {rotation[3]}" />',
                f'<attribute id="Scale" type="float" value="{scale}" />',
                '</node></children></node>'
        ]))
        transforms_map = target.find('./children/node[@id="Transforms"]')
        if not isinstance(transforms_map, et.Element):
            transforms_map = target.find('./children/node[@id="Transform"]')
            if not isinstance(transforms_map, et.Element):
                raise ValueError(f'cannot add a new transform to stage {stage_uuid} {to_compact_string(target)}')
        put_object_into_map(transforms_map, new_transform)

    def __put_transform_into_stage_lsx(
            self,
            target: et.Element,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float],
            scale: float,
            /,
            stage_uuid: str | None
    ) -> None:
        if stage_uuid is None:
            stage_uuid = self.__current_stage_uuid
        new_transform = et.fromstring(''.join([
                '<node id="Object">',
                f'<attribute id="MapKey" type="guid" value="{stage_uuid}" />',
                '<children><node id="MapValue">',
                f'<attribute id="Position" type="fvec3"><float3 x="{position[0]}" y="{position[1]}" z="{position[2]}"/></attribute>',
                f'<attribute id="RotationQuat" type="fvec4"><float4 x="{rotation[0]}" y="{rotation[1]}" z="{rotation[2]}" w="{rotation[3]}"/></attribute>',
                f'<attribute id="Scale" type="float" value="{scale}" />',
                '</node></children></node>'
        ]))
        transforms_map = target.find('./children/node[@id="Transforms"]')
        if not isinstance(transforms_map, et.Element):
            transforms_map = target.find('./children/node[@id="Transform"]')
            if not isinstance(transforms_map, et.Element):
                raise ValueError(f'cannot add a new transform to stage {stage_uuid} {to_compact_string(target)}')
        put_object_into_map(transforms_map, new_transform)
