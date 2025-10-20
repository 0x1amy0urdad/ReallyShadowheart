from __future__ import annotations

import anthropic as a
import decimal as dc
import io
import json
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
        return dc.Decimal(val)
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
        return dc.Decimal(val)
    return dc.Decimal(val).quantize(TIMELINE_DECIMAL_PRECISION)


def decimal_to_str(val: dc.Decimal) -> str:
    if val.is_zero():
        return '0'
    return str(val)


TIMELINE_DECIMAL_PRECISION = dc.Decimal('0.' + '0' * (TIMELINE_PRECISION - 1) + '1')
DECIMAL_ZERO = decimal_from_str('0')
DECIMAL_HALF = decimal_from_str('0.5')


def new_random_uuid() -> str:
    return str(uuid.uuid4())


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


def get_bg3_attribute(node: et.Element, attribute_name: str, /, value_name: str | None = None) -> str | None:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        return None
    effective_value_name = "value" if value_name is None else value_name
    return attribute_node.get(effective_value_name)


def get_required_bg3_attribute(node: et.Element, attribute_name: str, /, value_name: str | None = None) -> str:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't exist")
    effective_value_name = "value" if value_name is None else value_name
    value = attribute_node.get(effective_value_name)
    if value is None:
        raise ValueError(f"required BG3 attribute {attribute_name} doesn't have a value")
    return value


def get_bg3_handle_attribute(node: et.Element, attribute_name: str, /, value_name: str | None = None) -> tuple[str, int]:
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
        node: et.Element,
        attribute_name: str,
        attribute_value: str | float | int,
        /,
        attribute_type: str = "",
        version: int | None = None
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
        if version is not None:
            attribute_node = et.fromstring(f'<attribute id="{attribute_name}" type="{attribute_type}" handle="{value}" version="{version}" />')
        else:
            attribute_node = et.fromstring(f'<attribute id="{attribute_name}" type="{attribute_type}" value="{value}" />')
        node.append(attribute_node)
    else:
        if attribute_type:
            attribute_node.set("type", attribute_type)
        if version is None:
            attribute_node.set("value", value)
        else:
            attribute_node.set("handle", str(attribute_value))
            attribute_node.set("version", str(version))


def delete_bg3_attribute(node: et.Element, attribute_name: str) -> None:
    attribute_node = node.find(f'./attribute[@id="{attribute_name}"]')
    if attribute_node is None:
        raise ValueError(f"BG3 attribute {attribute_name} doesn't exist")
    node.remove(attribute_node)


def has_bg3_attribute(node: et.Element, attribute_name: str) -> bool:
    return node.find(f'./attribute[@id="{attribute_name}"]') is not None


def get_required_attribute(node: et.Element, attribute_name: str) -> str:
    result = node.get(attribute_name)
    if result is None:
        raise ValueError(f"required attribute {attribute_name} doesn't exist")
    return result


def lower_bound_by_node_attribute(nodes: list[et.Element], attribute_name: str, target_value: str) -> int:
    return lower_bound(nodes, lambda node: get_required_attribute(node, attribute_name), target_value)


def lower_bound_by_bg3_attribute(nodes: list[et.Element], attribute_name: str, target_value: str) -> int:
    return lower_bound(nodes, lambda node: get_required_bg3_attribute(node, attribute_name), target_value)


def lower_bound(nodes: list[et.Element], attribute_getter: Callable[[et.Element], str], target_value: str) -> int:
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


def find_object_by_map_key(target: et.Element, key: str) -> et.Element | None:
    objs = target.findall('./children/node[@id="Object"]')
    for obj in objs:
        obj_key = get_required_bg3_attribute(obj, 'MapKey')
        if key == obj_key:
            return obj
    return None


def put_object_into_map(target: et.Element, obj: et.Element) -> None:
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


def remove_object_by_map_key(target: et.Element, key: str) -> None:
    children = target.find('./children')
    if not isinstance(children, et.Element):
        raise KeyError(f"object '{key}' doesn't exist in the map")
    existing_obj = find_object_by_map_key(target, key)
    if existing_obj is None:
        raise KeyError(f"object '{key}' doesn't exist in the map")
    children.remove(existing_obj)


def get_or_create_child_node(parent_node: et.Element, chlild_node_id: str) -> et.Element:
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


def euler_to_quaternion(x_deg: float, y_deg: float, z_deg: float, sequence: str = 'xyz') -> tuple[float, float, float, float]:
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

def generate_ai_prompt_for_dialog_search(
        question: str,
        context: str,
        input_file_path: str,
        output_file_path: str | None = None
) -> str:
    if output_file_path is None:
        file_name = os.path.basename(input_file_path)
        dot_pos = file_name.rfind('.')
        if dot_pos > 0:
            file_name = file_name[:dot_pos]
        output_file_path = os.path.join(os.getcwd(), f'{file_name}.prompt.txt')
    with open(input_file_path, 'rt') as input_file:
        content = json.load(input_file)
    if not isinstance(content, list):
        raise TypeError(f'expected a list in {input_file_path}, got {type(content)}')
    context_lines = context.split('\n')
    prompt = '\n'.join([
        'This file contains a question, a description of a situation, and multiple possible answers.',
        'You task is to analyze the situation, and find up to 20 best fitting answers to the given question.',
        'You MUST NOT modify the answers, you MUST use them as is.',
        'The result of this task MUST contain (per each identified answer):',
        '1) a full unmodified answer,',
        '2) a quantative factor of how well it fits on scale from 0 to 100, and',
        '3) 1 or 2 sentences that explain why do you think this answer fits the given question and context.',
        f'The question is: "{question}".',
        f'The description of the situation:',
    ] + context_lines + [
        'The possible answers are listed below, 1 answer per line:'
    ])
    with open(output_file_path, 'wt') as output_file:
        output_file.write(prompt)
        for item in content:
            if not isinstance(item, dict):
                raise TypeError(f'expected a dict in {input_file_path}, got {type(content)}')
            for k, v in item.items():
                if isinstance(k, str) and isinstance(v, str):
                    if k != 'filename':
                        output_file.write(v)
                        output_file.write('\n')
    return output_file_path

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
        result.append(f"{attr.attrib['id']}={attr.attrib['value']}")
    return "|".join(result)
