from __future__ import annotations

import decimal as dc
import io
import numpy as np
import os
import uuid
import xml.etree.ElementTree as et

from typing import Any, Callable

# Precision of timestapms in timelines
TIMELINE_PRECISION = 4


def decimal_from_str(val: str | dc.Decimal) -> dc.Decimal:
    if isinstance(val, dc.Decimal):
        return val
    if isinstance(val, str):
        pos = val.find('.')
        if pos == -1:
            n = 0
            val += '.'
        else:
            n = len(val) - pos - 1
        while n < TIMELINE_PRECISION:
            val += '0'
            n += 1
        try:
            return dc.Decimal(val)
        except Exception as exc:
            raise RuntimeError(f'failed to convert: {val}') from exc
    raise TypeError(f'decimal_from_str() got an argument of an unexpected type: {type(val)}')


def decimal_from(val: str | dc.Decimal | float) -> dc.Decimal:
    if isinstance(val, dc.Decimal):
        return val
    if isinstance(val, str):
        pos = val.find('.')
        if pos == -1:
            n = 0
            val += '.'
        else:
            n = len(val) - pos - 1
        while n < TIMELINE_PRECISION:
            val += '0'
            n += 1
        try:
            return dc.Decimal(val)
        except Exception as exc:
            raise RuntimeError(f'failed to convert: {val}') from exc
    return dc.Decimal(val).quantize(TIMELINE_DECIMAL_PRECISION)


def decimal_to_str(val: dc.Decimal) -> str:
    if val.is_zero():
        return '0'
    return f'{val:f}'


TIMELINE_DECIMAL_PRECISION = dc.Decimal('0.' + '0' * (TIMELINE_PRECISION - 1) + '1')
DECIMAL_ZERO = decimal_from_str('0')
DECIMAL_HALF = decimal_from_str('0.5')


def new_random_uuid() -> str:
    return str(uuid.uuid4())


def new_random_handle() -> str:
    return 'h' + str(uuid.uuid4()).replace('-', 'g')


def translate_path(in_path: str) -> str:
    parts = in_path.replace('\\', '/').split('/')
    if ':' in parts[0]:
        parts[0] += "\\"
    return os.path.join(*parts)


def to_compact_string(xml_node: et.Element) -> str:
    return et.tostring(xml_node).decode('utf-8').replace('\t', '').replace('\n', '').replace('\r', '')


def get_len(iter: Any) -> int:
    if isinstance(iter, tuple) or isinstance(iter, list):
        return len(iter)
    if hasattr(iter, '__len__'):
        return iter.__len__()
    raise RuntimeError("Cannot determine lenght of an object")

def get_bg3_attribute(node: et.Element[str], attribute_name: str, /, value_name: str | None = None) -> str | None:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        return None
    if len(attribute_node) == 1:
        return ' '.join(get_lsx_vector_attribute(attribute_node))
    effective_value_name = "value" if value_name is None else value_name
    return attribute_node.get(effective_value_name)

def get_required_bg3_attribute(node: et.Element[str], attribute_name: str, /, value_name: str | None = None) -> str:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't exist")
    effective_value_name = "value" if value_name is None else value_name
    value = attribute_node.get(effective_value_name)
    if value is None:
        if len(attribute_node) == 1:
            return ' '.join(get_lsx_vector_attribute(attribute_node))
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't have a value")
    return value

def get_lsx_vector_attribute(attribute_node: et.Element[str]) -> tuple[str, ...]:
    if len(attribute_node) == 1:
        inner_node = attribute_node[0]
        if inner_node.tag == 'fvec2':
            x = inner_node.get('x')
            y = inner_node.get('y')
            if x is None or y is None:
                raise ValueError(f'unexpected None value: {to_compact_string(attribute_node)}')
            return (x, y)
        if inner_node.tag == 'fvec3':
            x = inner_node.get('x')
            y = inner_node.get('y')
            z = inner_node.get('z')
            if x is None or y is None or z is None:
                raise ValueError(f'unexpected None value: {to_compact_string(attribute_node)}')
            return (x, y, z)
        if inner_node.tag == 'fvec4':
            x = inner_node.get('x')
            y = inner_node.get('y')
            z = inner_node.get('z')
            w = inner_node.get('w')
            if x is None or y is None or z is None or w is None:
                raise ValueError(f'unexpected None value: {to_compact_string(attribute_node)}')
            return (x, y, z, w)
    raise RuntimeError(f'unexpected element: {to_compact_string(attribute_node)}, expected a fvec2 | fvec3 | fvec4 node')


def get_bg3_handle_attribute(node: et.Element[str], attribute_name: str, /, value_name: str | None = None) -> tuple[str, int]:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't exist")
    effective_value_name = "handle" if value_name is None else value_name
    value = attribute_node.get(effective_value_name)
    if value is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't have a value")
    version = attribute_node.get('version')
    if version is None:
        raise ValueError(f"BG3 text content {attribute_name} doesn't have a version")
    return (value, int(version))


def set_bg3_attribute(
        node: et.Element[str],
        attribute_name: str,
        attribute_value: str | float | int,
        /,
        attribute_type: str = "",
        version: int | None = None,
        lsx: bool  = False
    ) -> None:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if isinstance(attribute_value, float):
        value = str(dc.Decimal(str(attribute_value)).quantize(TIMELINE_DECIMAL_PRECISION))
    elif isinstance(attribute_value, int):
        value = str(attribute_value)
    elif isinstance(attribute_value, str):
        value = attribute_value
    else:
        raise TypeError(f'expected attribute_value of type str | float | int, got {type(attribute_value)}')
    if attribute_node is None:
        if not attribute_type:
            raise ValueError(f"attribute type is required to create a new attribute {attribute_name}")
        if lsx and attribute_type in {'fvec2', 'fvec3', 'fvec4'}:
            values = value.split(' ')
            if attribute_type == 'fvec2':
                if len(values) != 2:
                    raise RuntimeError(f'expected two numbers, got {attribute_value}')
                attribute_node = et.fromstring(
                    f'<attribute id="{attribute_name}" type="fvec2">' +
                    f'<float2 x="{values[0]}" y="{values[1]}" /></attribute>')
            elif attribute_type == 'fvec3':
                if len(values) != 3:
                    raise RuntimeError(f'expected three numbers, got {attribute_value}')
                attribute_node = et.fromstring(
                    f'<attribute id="{attribute_name}" type="fvec3">' +
                    f'<float3 x="{values[0]}" y="{values[1]} z="{values[2]}" /></attribute>')
            elif attribute_type == 'fvec4':
                if len(values) != 4:
                    raise RuntimeError(f'expected four numbers, got {attribute_value}')
                attribute_node = et.fromstring(
                    f'<attribute id="{attribute_name}" type="fvec4">' +
                    f'<float4 x="{values[0]}" y="{values[1]} z="{values[2]}" w="{values[3]}" /></attribute>')
        else:
            if version is not None:
                attribute_node = et.fromstring(f'<attribute id="{attribute_name}" type="{attribute_type}" handle="{value}" version="{version}" />')
            else:
                attribute_node = et.fromstring(f'<attribute id="{attribute_name}" type="{attribute_type}" value="{value}" />')
        node.append(attribute_node)
    else:
        if attribute_type:
            attribute_node.set('type', attribute_type)
        else:
            attribute_type = attribute_node.get('type')
        if lsx and attribute_type in {'fvec2', 'fvec3', 'fvec4'}:
            values = value.split(' ')
            if attribute_type == 'fvec2':
                if len(values) != 2:
                    raise RuntimeError(f'expected two numbers, got {attribute_value}')
                inner_node = attribute_node[0]
                if inner_node.tag != 'float2':
                    raise RuntimeError(f'expected float2 node, got {to_compact_string(attribute_node)}')
                inner_node.set('x', values[0])
                inner_node.set('y', values[1])
            elif attribute_type == 'fvec3':
                if len(values) != 3:
                    raise RuntimeError(f'expected three numbers, got {attribute_value}')
                inner_node = attribute_node[0]
                if inner_node.tag != 'float3':
                    raise RuntimeError(f'expected float3 node, got {to_compact_string(attribute_node)}')
                inner_node.set('x', values[0])
                inner_node.set('y', values[1])
                inner_node.set('z', values[2])
            elif attribute_type == 'fvec4':
                if len(values) != 4:
                    raise RuntimeError(f'expected four numbers, got {attribute_value}')
                inner_node = attribute_node[0]
                if inner_node.tag != 'float4':
                    raise RuntimeError(f'expected float4 node, got {to_compact_string(attribute_node)}')
                inner_node.set('x', values[0])
                inner_node.set('y', values[1])
                inner_node.set('z', values[2])
                inner_node.set('w', values[3])
        else:
            if version is None:
                attribute_node.set('value', value)
            else:
                attribute_node.set('handle', str(attribute_value))
                attribute_node.set('version', str(version))


def delete_bg3_attribute(node: et.Element[str], attribute_name: str) -> None:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        raise ValueError(f"BG3 attribute {attribute_name} doesn't exist")
    node.remove(attribute_node)


def has_bg3_attribute(node: et.Element[str], attribute_name: str) -> bool:
    return node.find(f'./attribute[@id="{attribute_name}"]') is not None


def get_required_attribute(node: et.Element[str], attribute_name: str) -> str:
    result = node.get(attribute_name)
    if result is None:
        raise ValueError(f"required attribute {attribute_name} doesn't exist")
    return result


def lower_bound_by_node_attribute(nodes: list[et.Element[str]], attribute_name: str, target_value: str) -> int:
    return lower_bound(nodes, lambda node: get_required_attribute(node, attribute_name), target_value)


def lower_bound_by_bg3_attribute(nodes: list[et.Element[str]], attribute_name: str, target_value: str) -> int:
    return lower_bound(nodes, lambda node: get_required_bg3_attribute(node, attribute_name), target_value)


def lower_bound(nodes: list[et.Element[str]], attribute_getter: Callable[[et.Element[str]], str], target_value: str) -> int:
    top = len(nodes)
    if top <= 1:
        return 0
    pos = top >> 1
    step = pos >> 1
    if step < 1:
        step = 1
    for n in range(0, top + 1):
        cur = attribute_getter(nodes[pos])
        next = None if pos + 1 >= top else attribute_getter(nodes[pos + 1])
        prev = None if pos == 0 else attribute_getter(nodes[pos - 1])
        if cur < target_value:
            if next is None or next > target_value:
                return pos
            if step > 1:
                step = step >> 1
            pos += step
        elif cur == target_value:
            return pos
        else:
            if prev is None or prev < target_value:
                return pos
            if step > 1:
                step = step >> 1
            pos -= step
    raise RuntimeError(f"Failed to find the lower bound for {target_value}")


def find_object_by_map_key(target: et.Element[str], key: str) -> et.Element | None:
    objs = target.findall('./children/node[@id="Object"]')
    for obj in objs:
        obj_key = get_required_bg3_attribute(obj, 'MapKey')
        if key == obj_key:
            return obj
    return None


def put_object_into_map(target: et.Element[str], obj: et.Element[str]) -> None:
    obj_key = get_required_bg3_attribute(obj, 'MapKey')
    children = target.find('./children')
    if children is None:
        children = et.fromstring('<children></children>')
        children.append(obj)
        target.append(children)
        return
    existing_obj = find_object_by_map_key(target, obj_key)
    if existing_obj is not None:
        children.remove(existing_obj)
    children.append(obj)


def remove_object_by_map_key(target: et.Element[str], key: str) -> None:
    children = target.find('./children')
    if not isinstance(children, et.Element[str]):
        raise KeyError(f"object '{key}' doesn't exist in the map")
    existing_obj = find_object_by_map_key(target, key)
    if existing_obj is None:
        raise KeyError(f"object '{key}' doesn't exist in the map")
    children.remove(existing_obj)


def get_or_create_child_node(parent_node: et.Element[str], chlild_node_id: str) -> et.Element[str]:
    children = parent_node.find('./children')
    if children is None:
        result = et.fromstring(f'<node id="{chlild_node_id}"></node>')
        children = et.fromstring(f'<children></children>')
        children.append(result)
        parent_node.append(children)
        return result
    node = children.find(f'./node[@id="{chlild_node_id}"]')
    if node is None:
        node = et.fromstring(f'<node id="{chlild_node_id}"></node>')
        children.append(node)
    return node


def normalize_voice_line(voice_line: str) -> str:
    skip = False
    voice_line = voice_line.lower().strip()
    result = []
    i = 0
    while i < len(voice_line):
        rem = len(voice_line) - i
        if rem > 4:
            tok = voice_line[i : i + 4]
            if tok == '&lt;':
                skip = True
                i += 4
                continue
            elif tok == '&gt;':
                skip = False
                i += 4
                continue
        if not skip:
            ch = voice_line[i]
            if ord(ch) >= 97 and ord(ch) <= 122:
                result.append(voice_line[i])
        i += 1
    return ''.join(result)


def print_and_write(f: io.TextIOWrapper, s: str | list[str]) -> None:
    if isinstance(s, str):
        print(s)
        f.write(s + '\n')
    elif isinstance(s, list):
        for l in s:
            print(l)
            f.write(l + '\n')
    else:
        raise TypeError()


def euler_to_quaternion(x_deg: float, y_deg: float, z_deg: float, sequence: str = 'yxz') -> tuple[float, float, float, float]:
    a1 = np.deg2rad(x_deg)
    a2 = np.deg2rad(y_deg)
    a3 = np.deg2rad(z_deg)

    a1_2 = a1 / 2
    a2_2 = a2 / 2
    a3_2 = a3 / 2

    c1 = np.cos(a1_2)
    s1 = np.sin(a1_2)
    c2 = np.cos(a2_2)
    s2 = np.sin(a2_2)
    c3 = np.cos(a3_2)
    s3 = np.sin(a3_2)

    calculations = {
        'xyz': lambda: (
            c1*c2*c3 - s1*s2*s3,  # w
            s1*c2*c3 + c1*s2*s3,  # x
            c1*s2*c3 - s1*c2*s3,  # y
            c1*c2*s3 + s1*s2*c3   # z
        ),
        'xzy': lambda: (
            c1*c2*c3 + s1*s2*s3,  # w
            s1*c2*c3 - c1*s2*s3,  # x
            c1*s2*c3 - s1*c2*s3,  # y
            c1*c2*s3 + s1*s2*c3   # z
        ),
        'yxz': lambda: (
            c1*c2*c3 + s1*s2*s3,  # w
            c1*s2*c3 + s1*c2*s3,  # x
            s1*c2*c3 - c1*s2*s3,  # y
            c1*c2*s3 - s1*s2*c3   # z
        ),
        'yzx': lambda: (
            c1*c2*c3 - s1*s2*s3,  # w
            c1*s2*c3 + s1*c2*s3,  # x
            s1*c2*c3 + c1*s2*s3,  # y
            c1*c2*s3 - s1*s2*c3   # z
        ),
        'zxy': lambda: (
            c1*c2*c3 - s1*s2*s3,  # w
            c1*c2*s3 + s1*s2*c3,  # x
            c1*s2*c3 + s1*c2*s3,  # y
            s1*c2*c3 - c1*s2*s3   # z
        ),
        'zyx': lambda: (
            c1*c2*c3 + s1*s2*s3,  # w
            c1*c2*s3 - s1*s2*c3,  # x
            c1*s2*c3 + s1*c2*s3,  # y
            s1*c2*c3 - c1*s2*s3   # z
        )
    }
    if sequence not in calculations:
        raise ValueError(f"rotation sequence '{sequence}' not supported")
    w, x, y, z = calculations[sequence]()

    norm = np.sqrt(w * w + x * x + y * y + z * z)
    return (round(float(x / norm), 9), round(float(y / norm), 9), round(float(z / norm), 9), round(float(w / norm), 9))

def quaternion_to_euler(x: float, y: float, z: float, w: float, sequence: str = 'xyz') -> tuple[float, float, float]:
    sequence = sequence.lower()

    r11 = 1         - 2 * y * y - 2 * z * z
    r12 = 2 * x * y - 2 * w * z
    r13 = 2 * x * z + 2 * w * y
    r21 = 2 * x * y + 2 * w * z
    r22 = 1         - 2 * x * x - 2 * z * z
    r23 = 2 * y * z - 2 * w * x
    r31 = 2 * x * z - 2 * w * y
    r32 = 2 * y * z + 2 * w * x
    r33 = 1         - 2 * x * x - 2 * y * y

    match sequence:
        case 'xyz':
            x_rad = np.arctan2(-r23, r33)
            y_rad = np.arcsin(r13)
            z_rad = np.arctan2(-r12, r11)
        case 'xzy':
            x_rad = np.arctan2(r32, r22)
            z_rad = np.arctan2(r13, r11)
            y_rad = np.arcsin(-r12)
        case 'yxz':
            y_rad = np.arcsin(-r23)
            x_rad = np.arctan2(r13, r33)
            z_rad = np.arctan2(r21, r22)
        case 'yzx':
            y_rad = np.arctan2(-r13, r11)
            z_rad = np.arctan2(-r23, r22)
            x_rad = np.arcsin(r21)
        case 'zxy':
            z_rad = np.arctan2(-r31, r33)
            x_rad = np.arcsin(r32)
            y_rad = np.arctan2(-r12, r22)
        case 'zyx':
            z_rad = np.arcsin(-r31)
            y_rad = np.arctan2(r32, r33)
            x_rad = np.arctan2(r21, r11)
        case _:
            raise ValueError(f"Rotation sequence '{sequence}' not supported")

    return round(float(np.rad2deg(x_rad)), 9), round(float(np.rad2deg(y_rad)), 9), round(float(np.rad2deg(z_rad)), 9)

def remove_all_nodes(node: et.Element[str]) -> None:
    children = node.find('./children')
    if children is None:
        return
    node.remove(children)
    node.append(et.fromstring('<children></children>'))

def attrs_to_str(node: et.Element[str]) -> str:
    result = list[str]()
    attrs = node.findall('./attribute')
    for attr in attrs:
        try:
            if 'value' in attr.attrib:
                result.append(f"{attr.attrib['id']}={attr.attrib['value']}")
            else:
                result.append(f"{attr.attrib['id']}={attr.attrib['handle']}:{attr.attrib['version']}")
        except KeyError as exc:
            raise KeyError(f'XML element: {et.tostring(attr)}') from exc
            
    return "|".join(result)

def find_bg3_appdata_path() -> str | None:
    local_appdata_path = os.getenv('LOCALAPPDATA')
    if local_appdata_path:
        bg3_appdata_path = os.path.join(local_appdata_path, 'Larian Studios', "Baldur's Gate 3")
        if os.path.isdir(bg3_appdata_path):
            return bg3_appdata_path
    return None
