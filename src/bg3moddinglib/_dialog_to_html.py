from __future__ import annotations

from base64 import b64encode
import datetime
import io
import multiprocessing as mp
import os
import sys
import time
import traceback
import xml.etree.ElementTree as et

from typing import Callable

from ._assets import bg3_assets
from ._common import (
    get_bg3_attribute,
    get_required_bg3_attribute,
    print_and_write,
)
from ._constants import *
from ._dialog import dialog_object
from ._files import game_file
from ._flags import flag_registry
from ._journal import journal
from ._loca import loca_object
from ._reactions import reaction_object
from ._skillchecks import difficulty_classes
from ._soundbank import soundbank_object
from ._tags import tag_registry
from ._timeline import timeline_object


PAD = ' ' * 4


UI_JAVASCRIPT = """
document.addEventListener("click", (event) => {
    const elt = document.elementFromPoint(event.clientX, event.clientY);
    if (elt.tagName == 'DIV' && elt.id) {
        elt.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'start' });
    }
});
window.addEventListener("load", (event) => {
    console.log('document loaded: ' + document.location);
    if (document.location.hash) {
        const node_uuid = document.location.hash.slice(1);
        const elt = document.getElementById(node_uuid);
        if (elt) {
            expand_node(node_uuid);
        }
    }
});
function get_expand_flags_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('expand-flags')) {
            return elt;
        }
    }
    return null;
}
function get_collapse_flags_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('collapse-flags')) {
            return elt;
        }
    }
    return null;
}
function get_flags_nodes(div_elt) {
    const result = [];
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('flags')) {
            result.push(elt);
        }
    }
    return result;
}
function on_click_expand_flags(uuid) {
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target: " + uuid);
        return;
    }
    get_expand_flags_elt(div_elt).classList.replace('visible', 'invisible')
    get_collapse_flags_elt(div_elt).classList.replace('invisible', 'visible')
    get_flags_nodes(div_elt).forEach(node => {
        node.classList.replace('invisible-flags', 'visible-flags')
    });
}
function on_click_collapse_flags(uuid) {
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target: " + uuid);
        return;
    }
    get_expand_flags_elt(div_elt).classList.replace('invisible', 'visible')
    get_collapse_flags_elt(div_elt).classList.replace('visible', 'invisible')
    get_flags_nodes(div_elt).forEach(node => {
        node.classList.replace('visible-flags', 'invisible-flags')
    });
}

function get_expand_nodecontext_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('expand-nodecontext')) {
            return elt;
        }
    }
    return null;
}
function get_collapse_nodecontext_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('collapse-nodecontext')) {
            return elt;
        }
    }
    return null;
}
function get_nodecontext_nodes(div_elt) {
    const result = [];
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('nodecontext')) {
            result.push(elt);
        }
    }
    return result;
}
function on_click_expand_nodecontext(uuid) {
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target: " + uuid);
        return;
    }
    get_expand_nodecontext_elt(div_elt).classList.replace('visible', 'invisible')
    get_collapse_nodecontext_elt(div_elt).classList.replace('invisible', 'visible')
    get_nodecontext_nodes(div_elt).forEach(node => {
        node.classList.replace('invisible-nodecontext', 'visible-nodecontext')
    });
}
function on_click_collapse_nodecontext(uuid) {
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target: " + uuid);
        return;
    }
    get_expand_nodecontext_elt(div_elt).classList.replace('invisible', 'visible')
    get_collapse_nodecontext_elt(div_elt).classList.replace('visible', 'invisible')
    get_nodecontext_nodes(div_elt).forEach(node => {
        node.classList.replace('visible-nodecontext', 'invisible-nodecontext')
    });
}

function get_expand_children_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('expand-children')) {
            return elt;
        }
    }
    return null;
}
function get_collapse_children_elt(div_elt) {
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('collapse-children')) {
            return elt;
        }
    }
    return null;
}
function get_children_nodes(div_elt) {
    const result = [];
    for (let i = 0; i < div_elt.children.length; ++i) {
        const elt = div_elt.children[i];
        if (elt.classList.contains('node')) {
            result.push(elt);
        }
    }
    return result;
}
function on_click_expand_children(uuid) {
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target: " + uuid);
        return;
    }
    get_expand_children_elt(div_elt).classList.replace('visible', 'invisible')
    get_collapse_children_elt(div_elt).classList.replace('invisible', 'visible')
    get_children_nodes(div_elt).forEach(node => {
        node.classList.replace('invisible-node', 'visible-node')
    });
}
function on_click_collapse_children(uuid) {
    const div_elt = document.getElementById(uuid);
    if (div_elt == null) {
        console.log("Can't find parent of the click target: " + uuid);
        return;
    }
    get_expand_children_elt(div_elt).classList.replace('invisible', 'visible')
    get_collapse_children_elt(div_elt).classList.replace('visible', 'invisible')
    get_children_nodes(div_elt).forEach(node => {
        node.classList.replace('visible-node', 'invisible-node')
    });
}
function expand_one_node(node_elt) {
    var e = get_expand_flags_elt(node_elt);
    if (e) {
        e.classList.replace('visible', 'invisible');
    }
    e = get_collapse_flags_elt(node_elt);
    if (e) {
        e.classList.replace('invisible', 'visible');
    }
    e = get_flags_nodes(node_elt);
    if (e) {
        e.forEach(node => {
            node.classList.replace('invisible-flags', 'visible-flags')
        });
    }

    e = get_expand_nodecontext_elt(node_elt);
    if (e) {
        e.classList.replace('visible', 'invisible');
    }
    e = get_collapse_nodecontext_elt(node_elt);
    if (e) {
        e.classList.replace('invisible', 'visible');
    }
    e = get_nodecontext_nodes(node_elt);
    if (e) {
        e.forEach(node => {
            node.classList.replace('invisible-nodecontext', 'visible-nodecontext')
        });
    }

    e = get_expand_children_elt(node_elt);
    if (e) {
        e.classList.replace('visible', 'invisible')
    }
    e = get_collapse_children_elt(node_elt);
    if (e) {
        e.classList.replace('invisible', 'visible')
    }
    e = get_children_nodes(node_elt);
    if (e) {
        e.forEach(node => {
            node.classList.replace('invisible-node', 'visible-node')
        });
    }
}
function expand_node(uuid) {
    const target_uuid = uuid;
    const target_elt = document.getElementById(uuid);
    if (target_elt == null) {
        console.log("Can't find parent of the click target: " + uuid);
        return false;
    }
    var node_uuid = target_elt.getAttribute('name');
    console.log("node_uuid = " + node_uuid);
    while (node_uuid != 'toplevelnode') {
        const node_elt = document.getElementById(node_uuid);
        if (node_elt == null) {
            console.log("Node cannot be found: " + node_uuid);
            break;
        }
        expand_one_node(node_elt);
        node_uuid = node_elt.getAttribute('name');
    }
    target_elt.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'start' });
    return false;
}
function expand_all() {
    const nodes = document.getElementsByClassName('node');
    for (var i = 0; i < nodes.length; ++i) {
        expand_one_node(nodes.item(i));
    }
}
function collapse_one_node(node_elt) {
    var e = get_expand_flags_elt(node_elt);
    if (e) {
        e.classList.replace('invisible', 'visible');
    }
    e = get_collapse_flags_elt(node_elt);
    if (e) {
        e.classList.replace('visible', 'invisible');
    }
    e = get_flags_nodes(node_elt);
    if (e) {
        e.forEach(node => {
            node.classList.replace('visible-flags', 'invisible-flags')
        });
    }

    e = get_expand_nodecontext_elt(node_elt);
    if (e) {
        e.classList.replace('invisible', 'visible');
    }
    e = get_collapse_nodecontext_elt(node_elt);
    if (e) {
        e.classList.replace('visible', 'invisible');
    }
    e = get_nodecontext_nodes(node_elt);
    if (e) {
        e.forEach(node => {
            node.classList.replace('visible-nodecontext', 'invisible-nodecontext')
        });
    }

    e = get_expand_children_elt(node_elt);
    if (e) {
        e.classList.replace('invisible', 'visible')
    }
    e = get_collapse_children_elt(node_elt);
    if (e) {
        e.classList.replace('visible', 'invisible')
    }
    e = get_children_nodes(node_elt);
    if (e) {
        e.forEach(node => {
            node.classList.replace('visible-node', 'invisible-node')
        });
    }
}
function collapse_all() {
    const nodes = document.getElementsByClassName('node');
    for (var i = 0; i < nodes.length; ++i) {
        collapse_one_node(nodes.item(i));
    }
}

function expand_all_flags() {
    const nodes = document.getElementsByClassName('node');
    for (var i = 0; i < nodes.length; ++i) {
        const node_elt = nodes.item(i);
        var e = get_expand_flags_elt(node_elt);
        if (e) {
            e.classList.replace('visible', 'invisible');
        }
        e = get_collapse_flags_elt(node_elt);
        if (e) {
            e.classList.replace('invisible', 'visible');
        }
        e = get_flags_nodes(node_elt);
        if (e) {
            e.forEach(node => {
                node.classList.replace('invisible-flags', 'visible-flags')
            });
        }
    }
}

function collapse_all_flags() {
    const nodes = document.getElementsByClassName('node');
    for (var i = 0; i < nodes.length; ++i) {
        const node_elt = nodes.item(i);
        var e = get_expand_flags_elt(node_elt);
        if (e) {
            e.classList.replace('invisible', 'visible');
        }
        e = get_collapse_flags_elt(node_elt);
        if (e) {
            e.classList.replace('visible', 'invisible');
        }
        e = get_flags_nodes(node_elt);
        if (e) {
            e.forEach(node => {
                node.classList.replace('visible-flags', 'invisible-flags')
            });
        }
    }
}

function expand_all_nodecontexts() {
    const nodes = document.getElementsByClassName('node');
    for (var i = 0; i < nodes.length; ++i) {
        const node_elt = nodes.item(i);
        var e = get_expand_nodecontext_elt(node_elt);
        if (e) {
            e.classList.replace('visible', 'invisible');
        }
        e = get_collapse_nodecontext_elt(node_elt);
        if (e) {
            e.classList.replace('invisible', 'visible');
        }
        e = get_nodecontext_nodes(node_elt);
        if (e) {
            e.forEach(node => {
                node.classList.replace('invisible-nodecontext', 'visible-nodecontext')
            });
        }
    }
}

function collapse_all_nodecontexts() {
    const nodes = document.getElementsByClassName('node');
    for (var i = 0; i < nodes.length; ++i) {
        const node_elt = nodes.item(i);
        var e = get_expand_nodecontext_elt(node_elt);
        if (e) {
            e.classList.replace('invisible', 'visible');
        }
        e = get_collapse_nodecontext_elt(node_elt);
        if (e) {
            e.classList.replace('visible', 'invisible');
        }
        e = get_nodecontext_nodes(node_elt);
        if (e) {
            e.forEach(node => {
                node.classList.replace('visible-nodecontext', 'invisible-nodecontext')
            });
        }
    }
}
"""


class dialog_to_html:
    __assets: bg3_assets
    __textbank: loca_object
    __mod_textbank: loca_object | None
    __extra_textbank: loca_object | None
    __soundbanks: dict[str, soundbank_object]
    __mod_soundbanks: dict[str, soundbank_object]
    __extra_soundbanks: dict[str, soundbank_object]
    __flags: flag_registry
    __tags: tag_registry
    __journal: journal
    __dcs: difficulty_classes
    __known_nodes: dict[str, int]
    __referenced_nodes: dict[str, int]
    __node_index: dict[str, tuple[str, ...]]
    __root_dir_path: str
    __relative_file_path: str

    def __init__(self, a: bg3_assets) -> None:
        self.__assets = a
        self.__textbank = loca_object(a.files.get_text_bank_file())
        self.__mod_textbank = None
        self.__extra_textbank = None
        self.__soundbanks = dict[str, soundbank_object]()
        self.__mod_soundbanks = dict[str, soundbank_object]()
        self.__extra_soundbanks = dict[str, soundbank_object]()
        self.__flags = flag_registry(a.files.tool)
        self.__tags = tag_registry(a.files.tool)
        self.__journal = journal(a.files.tool)
        self.__dcs = difficulty_classes(a.files.tool)
        self.__known_nodes = dict[str, int]()
        self.__referenced_nodes = dict[str, int]()
        self.__node_index = dict[str, tuple[str, ...]]()
        self.__root_dir_path = ''
        self.__relative_file_path = ''


    @property
    def assets(self) -> bg3_assets:
        return self.__assets


    def start_dialog_html_file(self, d: dialog_object, e: dict[str, str], f: io.TextIOWrapper, extra_lines: list[str]) -> None:
        try:
            lsf_path = f'{self.__assets.index.get_pak_by_file(e['lsf_path'])}:{e['lsf_path']}'
        except:
            lsf_path = 'not found'
        try:
            lsj_path = f'{self.__assets.index.get_pak_by_file(e['lsj_path'])}:{e['lsj_path']}'
        except:
            lsj_path = 'not found'
        try:
            dialog_bank_path = f'{e['dialog_bank_pak']}:{e['dialog_bank_path']}'
        except:
            dialog_bank_path = 'not found'
        try:
            dialog_uuid = e['dialog_uuid']
        except:
            dialog_uuid = 'unknown'
        try:
            timeline_uuid = e['timeline_uuid']
        except:
            timeline_uuid = 'unknown'
        lines = []
        for extra_line in extra_lines:
            lines.append(f'{PAD}{PAD}<div class="synopsis"><label>{extra_line}</label></div>')
        f.write("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>""" + d.name + """</title>
        <style>
            body {
                background-color: lightgrey;
                font-family: monospace;
                font-size: medium;
            }
            .title {
                font-family: 'Times New Roman', Times, serif;
                font-size: xx-large;
                display: block;
                padding: 10px 0px 10px 10px;
            }
            .synopsis {
                font-family: 'Times New Roman', Times, serif;
                font-size: medium;
                display: block;
                padding: 10px 0px 10px 10px;
            }
            .greeting {
                background-color: white;
            }
            .question {
                background-color: lightgreen;
            }
            .answer {
                background-color: azure;
            }
            .cinematic {
                background-color: lightpink;
            }
            .visualstate {
                background-color: plum;
            }
            .nested {
                background-color: salmon;
            }
            .jump {
                background-color: khaki;
            }
            .alias {
                background-color: peachpuff;
            }
            .activeroll {
                background-color: lavender;
            }
            .passiveroll {
                background-color: lightcyan;
            }
            .rollresult {
                background-color: lightblue;
            }
            .empty {
                background-color: cornsilk;
            }
            .trade {
                background-color: lightyellow;
            }
            .pop {
                background-color: white;
            }
            .other {
                background-color: white;
            }
            .link {
                background-color: whitesmoke;
            }
            .visible {
                display: inline;
            }
            .invisible {
                display: none;
            }
            .visible-flags {
                display: block;
                margin: 5px 0px 5px 5px;
            }
            .invisible-flags {
                display: none;
            }
            .visible-nodecontext {
                display: block;
                margin: 5px 0px 5px 5px;
            }
            .invisible-nodecontext {
                display: none;
            }
            .visible-node {
                display: block;
            }
            .invisible-node {
                display: none;
            }
            .expand-nodecontext {
                cursor: pointer;
            }
            .collapse-nodecontext {
                cursor: pointer;
            }
            .expand-flags {
                cursor: pointer;
            }
            .collapse-flags {
                cursor: pointer;
            }
            .expand-children {
                cursor: pointer;
            }
            .collapse-children {
                cursor: pointer;
            }
            .info {
                font-style: normal;
                font-weight: normal;
            }
            .speaker {
                font-style: normal;
                font-weight: normal;
            }
            .reactions {
                font-style: normal;
                font-weight: normal;
            }
            .voiceline {
                font-style: normal;
                font-family: Arial, Helvetica, sans-serif;
                font-size: medium;
                font-weight: normal;
                cursor: pointer;
            }
            .node {
                width: auto;
                height: 100%;
                padding: 8px 0px 8px 8px;
                margin: 8px 0px 8px 8px;
                border: thin dotted;
            }
            .clipboard {
                cursor: pointer;
            }
            .control {
                cursor: pointer;
                text-decoration: underline dotted;
                text-decoration-color: blue;
            }
            .right {
                float: right;
            }
            .actions {
                margin: 16px 0px 16px 16px;
            }
            .notext {
                font-size: 0;
            }
            .flag {
                font-size: medium;
            }
            .flags {
            }
            .checkflags {
            }
            .setflags {
            }
            .flaggroup {
            }
        </style>
        <script type="text/javascript">
    """ + UI_JAVASCRIPT + f"""
        </script>
    </head>
    <body>
        <div class="title">{d.name}</div>
    """ + '\n'.join(lines) + f"""
        <div><label>Dialog UUID:&nbsp;</label><label class="clipboard" onclick="navigator.clipboard.writeText('{dialog_uuid}')">{dialog_uuid}</label></div>
        <div><label>Timeline UUID:&nbsp;</label><label class="clipboard" >{timeline_uuid}</label></div>
        <div><label>LSJ path: {lsj_path}</label></div>
        <div><label>LSF path: {lsf_path}</label></div>
        <div><label>Dialog bank path: {dialog_bank_path}</label></div>
        <div class="actions">
            <span><label>   |   </label></span>
            <span><label class="control" onclick="expand_all()">Click here to EXPAND ALL</label></span>
            <span><label>   |   </label></span>
            <span><label class="control" onclick="collapse_all()">Click here to COLLAPSE ALL</label></span>            
            <span><label>   |   </label></span>
            <span><label class="control" onclick="expand_all_flags()">Click here to EXPAND ALL FLAGS</label></span>
            <span><label>   |   </label></span>
            <span><label class="control" onclick="collapse_all_flags()">Click here to COLLAPSE ALL FLAGS</label></span>            
            <span><label>   |   </label></span>
            <span><label class="control" onclick="expand_all_nodecontexts()">Click here to EXPAND ALL NODE CONTEXTS</label></span>
            <span><label>   |   </label></span>
            <span><label class="control" onclick="collapse_all_nodecontexts()">Click here to COLLAPSE ALL NODE CONTEXTS</label></span>            
            <span><label>   |   </label></span>
        </div>
    """)


    def finish_dialog_html_file(self, f: io.TextIOWrapper) -> None:
        f.write("""
    </body>
</html>""")


    def convert_dialog_node_to_html(
            self,
            d: dialog_object,
            d_editor_ctx: dialog_object | None,
            t: timeline_object | None,
            node_uuid: str,
            parent_node_uuid: str,
            visible: bool,
            f: io.TextIOWrapper,
            outer_padding: str,
            /,
            is_orphan: bool = False
    ) -> None:
        node = d.find_dialog_node(node_uuid)
        node_css = ['node', 'visible-node' if visible else 'invisible-node']
        inner_padding = f'{outer_padding}{PAD}'

        if not parent_node_uuid:
            parent_node_uuid = "toplevelnode"

        if node_uuid in self.__known_nodes:
            n = self.__known_nodes[node_uuid]
            self.__known_nodes[node_uuid] = n + 1
            node_css.append('link')
            html_lines = [
                f'{outer_padding}<div id="{node_uuid}_{n}" name="{parent_node_uuid}" class="{' '.join(node_css)}">',
                f'{inner_padding}<a href="#{node_uuid}" onclick="expand_node(\'{node_uuid}\')">Link to node {node_uuid}</a>',
                f'{outer_padding}</div>'
            ]
            f.write('\n'.join(html_lines))
            f.write('\n')
            return

        self.__known_nodes[node_uuid] = 1
        texts_with_rules = d.get_tagged_texts_with_rules(node_uuid)
        non_empty = len(texts_with_rules) > 0
        ctor = get_required_bg3_attribute(node, 'constructor')
        match ctor:
            case 'TagGreeting':
                node_css.append('greeting')
            case 'TagQuestion':
                node_css.append('question')
            case 'TagAnswer':
                node_css.append('answer' if non_empty else 'empty')
            case 'SelectSpeaker':
                node_css.append('answer' if non_empty else 'empty')
            case 'TagCinematic':
                node_css.append('cinematic')
            case 'Visual State':
                node_css.append('visualstate')
            case 'Nested Dialog':
                node_css.append('nested')
            case 'Jump':
                node_css.append('jump')
            case 'Alias':
                node_css.append('alias')
            case 'ActiveRoll':
                node_css.append('activeroll')
            case 'PassiveRoll':
                node_css.append('passiveroll')
            case 'RollResult':
                node_css.append('rollresult')
            case 'Pop':
                node_css.append('pop')
            case 'Trade':
                node_css.append('trade')
            case 'State':
                node_css.append('other')
            case 'FallibleQuestionResult':
                node_css.append('other')
            case _:
                raise RuntimeError(f'unsupported dialog node constructor: {ctor}')
        html_lines = [f'{outer_padding}<div id="{node_uuid}" name="{parent_node_uuid}" class="{' '.join(node_css)}">']
        if is_orphan:
            html_lines.append(f'{inner_padding}<div class="orphan">')
            html_lines.append(f'{inner_padding}{PAD}<label>ORPHANED NODE</label>')
            html_lines.append(f'{inner_padding}</div>')
        html_lines += self.get_info_lines(d, t, node, node_uuid, parent_node_uuid, ctor, inner_padding)

        reactions = self.get_reactions_line(node, inner_padding)
        if reactions:
            html_lines.append(reactions)

        if ctor == 'Alias':
            source_node_uuid = get_required_bg3_attribute(node, 'SourceNode')
            source_node = d.find_dialog_node(source_node_uuid)
            speaker_idx = get_bg3_attribute(source_node, 'speaker')
            texts_with_rules = d.get_tagged_texts_with_rules(source_node_uuid)
        else:
            source_node = None
            speaker_idx = get_bg3_attribute(node, 'speaker')

        if speaker_idx:
            try:
                speaker_name = self.get_speaker_name_by_slot_index(d, speaker_idx)
            except:
                speaker_name = f'Speaker {speaker_idx}'
            if speaker_name:
                question = False
                if ctor == 'TagQuestion':
                    question = True
                speaker_uuid = None
                if speaker_idx == '-666':
                    speaker_uuid = 'NARRATOR'
                else:
                    try:
                        speaker_uuid = d.get_speaker_by_index(int(speaker_idx))
                    except:
                        speaker_uuid = None
                text_lines = self.get_text_lines(speaker_uuid, node_uuid, texts_with_rules, f'{inner_padding}{PAD}', question)
                html_lines.append(f'{inner_padding}<div class="speaker" name="{speaker_idx}">')
                if text_lines:
                    html_lines.append(f'{inner_padding}{PAD}<label class="speaker">{speaker_name} [{speaker_idx}]</label><label> says:</label><br>')
                    html_lines += text_lines
                elif ctor == 'Trade':
                    html_lines.append(f'{inner_padding}{PAD}<label class="speaker">Trader: {speaker_name} [{speaker_idx}]</label><br>')
                else:
                    html_lines.append(f'{inner_padding}{PAD}<label class="speaker">{speaker_name} [{speaker_idx}]</label><label> says nothing</label><br>')
                html_lines.append(f'{inner_padding}</div>')

        if d_editor_ctx:
            context_lines = self.get_node_context_lines(d_editor_ctx, node_uuid, inner_padding)
            if context_lines:
                html_lines += context_lines

        checkflags_groups = node.findall('./children/node[@id="checkflags"]/children/node[@id="flaggroup"]')
        setflags_groups = node.findall('./children/node[@id="setflags"]/children/node[@id="flaggroup"]')
        if setflags_groups or checkflags_groups:
            html_lines.append(f'{inner_padding}<label class="expand-flags visible" onclick="on_click_expand_flags(\'{node_uuid}\')">[+]</label>')
            html_lines.append(f'{inner_padding}<label class="collapse-flags invisible" onclick="on_click_collapse_flags(\'{node_uuid}\')">[-]</label>')
            html_lines.append(f'{inner_padding}<label> <strong>Flags</strong></label><br>')
            if checkflags_groups:
                html_lines.append(f'{inner_padding}<div class="invisible-flags checkflags flags">')
                for checkflags_group in checkflags_groups:
                    html_lines += self.get_flag_group_lines(d, checkflags_group, False, f'{inner_padding}{PAD}')
                html_lines.append(f'{inner_padding}</div>')

            if setflags_groups:
                html_lines.append(f'{inner_padding}<div class="invisible-flags setflags flags">')
                for setflags_group in setflags_groups:
                    html_lines += self.get_flag_group_lines(d, setflags_group, True, f'{inner_padding}{PAD}')
                html_lines.append(f'{inner_padding}</div>')

        children = node.findall('./children/node[@id="children"]/children/node[@id="child"]')
        if len(children) > 0:
            html_lines.append(f'{inner_padding}<label class="expand-children visible" onclick="on_click_expand_children(\'{node_uuid}\')">[+]</label>')
            html_lines.append(f'{inner_padding}<label class="collapse-children invisible" onclick="on_click_collapse_children(\'{node_uuid}\')">[-]</label>')
            if len(children) == 1:
                html_lines.append(f'{inner_padding}<label>1 child node</label><br>')
            else:
                html_lines.append(f'{inner_padding}<label>{len(children)} children nodes</label><br>')

        try:
            f.write('\n'.join(html_lines))
        except Exception as ex:
            print(f'node uuid = {node_uuid}')
            print(html_lines)
            raise ex
        f.write('\n')
        for child_node in children:
            child_node_uuid = get_required_bg3_attribute(child_node, 'UUID')
            self.convert_dialog_node_to_html(d, d_editor_ctx, t, child_node_uuid, node_uuid, False, f, inner_padding)
        f.write(f'{outer_padding}</div>\n')


    def get_info_lines(
            self,
            d: dialog_object,
            t: timeline_object | None,
            dialog_node: et.Element[str],
            node_uuid: str,
            parent_node_uuid: str,
            ctor: str,
            padding: str
    ) -> list[str]:
        root = get_bg3_attribute(dialog_node, 'Root') == 'True'
        endnode = get_bg3_attribute(dialog_node, 'endnode') == 'True'
        showonce = get_bg3_attribute(dialog_node, 'ShowOnce') == 'True'
        transitionmode = get_bg3_attribute(dialog_node, 'transitionmode') == '2'
        group_id = get_bg3_attribute(dialog_node, 'GroupID')
        group_index = get_bg3_attribute(dialog_node, 'GroupIndex')

        description = []
        if t is not None:
            phase_index = t.get_timeline_phase_index(node_uuid)
            if phase_index is not None:
                description.append('timeline phase index ' + str(phase_index))

        description += [
            'RootNode' if root else '',
            'EndNode' if endnode else '',
            'ShowOnce' if showonce else '',
            'TransitionMode2' if transitionmode else '',
        ]
        if group_id:
            description.append(f'<a href="#{group_id}">Group {group_id}, index {group_index}</a>')

        result = []
        result.append(f'{padding}<div class="info">')
        result.append(f'{padding}{PAD}<label><strong>{ctor}</strong> {' | '.join([e for e in description if e])}</label>')

        if ctor == 'Jump':
            jump_target = get_required_bg3_attribute(dialog_node, 'jumptarget')
            jump_target_point = get_required_bg3_attribute(dialog_node, 'jumptargetpoint')
            result.append(f'{padding}{PAD}<label> to </label>')
            result.append(f'{padding}{PAD}<a href="#{jump_target}" onclick="expand_node(\'{jump_target}\')">{jump_target}</a>')
            result.append(f'{padding}{PAD}<label> after voice line</label>' if jump_target_point == '2' else f'{padding}{PAD}<label> before voice line</label>')

        if ctor == 'Alias':
            source_node = get_required_bg3_attribute(dialog_node, 'SourceNode')
            result.append(f'{padding}{PAD}<label> source node </label>')
            result.append(f'{padding}{PAD}<a href="#{source_node}" onclick="expand_node(\'{source_node}\')">{source_node}</a>')

        if ctor == 'Nested Dialog':
            nested_dialog_uuid = get_required_bg3_attribute(dialog_node, 'NestedDialogNodeUUID')
            dialog_name = self.__assets.index.get_dialog_name(nested_dialog_uuid)
            e = self.__assets.index.get_entry(dialog_name)

            if 'lsj_path' in e and e['lsj_path']:
                pos = e['lsj_path'].rfind('/')
                file_name = e['lsj_path'][pos + 1: -4] + '.html'

                path_pos = e['lsj_path'].find('/Story/Dialogs/')
                dirs = e['lsj_path'][path_pos + 15: pos].split('/')
            elif 'lsf_path' in e and e['lsf_path']:
                pos = e['lsf_path'].rfind('/')
                file_name = e['lsf_path'][pos + 1: -4] + '.html'

                path_pos = e['lsf_path'].find('/Story/DialogsBinary/')
                dirs = e['lsf_path'][path_pos + 21: pos].split('/')
            else:
                raise RuntimeError(f'cannot determine nested dialog file path for {nested_dialog_uuid}')
            
            nested_dialog_file_path = os.path.join(self.__root_dir_path, *dirs, file_name)

            result.append(f'{padding}{PAD}<a href="{nested_dialog_file_path}">{dialog_name}</a>')

        if ctor == 'ActiveRoll' or ctor == 'PassiveRoll':
            roll_type = get_required_bg3_attribute(dialog_node, 'RollType')
            roll_ability = get_required_bg3_attribute(dialog_node, 'Ability')
            roll_skill = get_required_bg3_attribute(dialog_node, 'Skill')
            roll_target = get_required_bg3_attribute(dialog_node, 'RollTargetSpeaker')
            roll_advantage = get_required_bg3_attribute(dialog_node, 'Advantage')
            roll_advantage_reason = get_bg3_attribute(dialog_node, 'AdvantageReason', value_name = 'handle')
            if roll_advantage_reason:
                try:
                    roll_advantage_reason = self.__textbank.get_line(roll_advantage_reason)
                except:
                    roll_advantage_reason = f'unknown string {roll_advantage_reason}'
            roll_exclude_companion_bonus = get_bg3_attribute(dialog_node, 'ExcludeCompanionsOptionalBonuses') == 'True'
            roll_exclude_player_bonus = get_bg3_attribute(dialog_node, 'ExcludeSpeakerOptionalBonuses') == 'True'
            roll_dc_id = get_bg3_attribute(dialog_node, 'DifficultyClassID')
            if roll_dc_id:
                try:
                    dc = self.__dcs.get_dc(roll_dc_id)
                    roll_dc_name = dc.name
                    roll_dc_val = dc.difficulty
                except:
                    roll_dc_name = ''
                    roll_dc_val = ''
            else:
                roll_dc_name = ''
                roll_dc_val = int(get_required_bg3_attribute(dialog_node, 'DifficultyClass'))
            if roll_skill:
                roll_ability = roll_ability + '/' + roll_skill
            roll_target_speaker = self.get_speaker_name_by_slot_index(d, roll_target)
            roll_extras = []
            if roll_advantage == 1:
                if roll_advantage_reason:
                    roll_extras.append(f'with advantage ({roll_advantage_reason})')
                else:
                    roll_extras.append('with advantage')
                if roll_exclude_companion_bonus:
                    roll_extras.append('exclude companion bonus')
                if roll_exclude_player_bonus:
                    roll_extras.append('exclude player bonus')
            result.append(f'{padding}{PAD}<label> | {roll_type} {roll_ability} {roll_dc_name} DC{roll_dc_val} targeting speaker {roll_target} {roll_target_speaker} | {'|'.join(roll_extras)}')

        if ctor == 'RollResult':
            success = get_required_bg3_attribute(dialog_node, 'Success')
            if success == 'True':
                result.append(f'{padding}{PAD}<label> SUCCESS</label>')
            else:
                result.append(f'{padding}{PAD}<label> FAILURE</label>')

        result.append(f'{padding}{PAD}<span class="right"><a href="#{parent_node_uuid}">TO PARENT NODE</a><label> | </label><label class="clipboard" onclick="navigator.clipboard.writeText(\'{node_uuid}\')"><i>{node_uuid}</i> |</label></span>')
        result.append(f'{padding}</div>')
        return result


    def get_reactions_line(self, dialog_node: et.Element[str], padding: str) -> str:
        approval_rating_id = get_bg3_attribute(dialog_node, 'ApprovalRatingID')
        if approval_rating_id:
            try:
                r = reaction_object.open_existing(self.__assets.files, approval_rating_id).pretty_reactions.items()
            except:
                return f'{padding}<label class="reactions">Reactions: missing reaction {approval_rating_id}</label>'
        else:
            reactions = dialog_node.findall('./children/node[@id="GameData"]/children/node[@id="ApprovalRatingDatas"]')
            if reactions:
                r = {
                    self.__assets.index.get_character_name(get_required_bg3_attribute(reaction, 'ApprovalSpeaker')) : int(get_required_bg3_attribute(reaction, 'ApprovalAmount'))
                    for reaction in reactions
                }.items()
            else:
                return ''
        return f'{padding}<label class="reactions clipboard" onclick="navigator.clipboard.writeText(\'{approval_rating_id}\')">Reactions: ' + ' | '.join([f'{character} {approval:+}' for character, approval in r if approval != 0]) + '</label>'


    def get_node_context_lines(self, d: dialog_object, dialog_node_uuid: str, padding: str) -> list[str]:
        dialog_node = d.find_dialog_node(dialog_node_uuid)
        nodes = dialog_node.findall('./children/node[@id="editorData"]/children/node')
        lines = list[str]()
        context_nodes = frozenset(['CinematicNodeContext', 'InternalNodeContext', 'NodeContext', 'VOContext', 'VOContextAfter'])
        for node in nodes:
            key = get_bg3_attribute(node, 'key')
            val = get_bg3_attribute(node, 'val')
            if key in context_nodes and val:
                lines.append(f'{padding}{PAD}<div><label>{key}: {val}<label></div>')
        if lines:
            result = [
                f'{padding}<label class="expand-nodecontext visible" onclick="on_click_expand_nodecontext(\'{dialog_node_uuid}\')">[+]</label>',
                f'{padding}<label class="collapse-nodecontext invisible" onclick="on_click_collapse_nodecontext(\'{dialog_node_uuid}\')">[-]</label>',
                f'{padding}<label> <strong>Node context</strong></label><br>',
                f'{padding}<div class="nodecontext invisible-nodecontext">']
            result += lines
            result.append(f'{padding}</div>')
            return result
        return []


    def get_speaker_name_by_slot_index(self, d: dialog_object, slot_index: str) -> str | None:
        if slot_index == '-666':
            speaker_name = 'Narrator'
        elif slot_index == '-1':
            speaker_name = None
        else:
            speaker = d.get_speaker_by_index(int(slot_index))
            speaker_name = self.__assets.index.get_character_name(speaker)
            if not speaker_name:
                speaker_name = f'Speaker_{speaker}'
        return speaker_name


    def __get_translated_string(self, handle: str) -> str:
        result = ''
        try:
            result = self.__textbank.get_line(handle)
        except:
            result = ''
        if not result and self.__mod_textbank:
            try:
                result = self.__mod_textbank.get_line(handle)
            except:
                result = ''
        if not result and self.__extra_textbank:
            try:
                result = self.__extra_textbank.get_line(handle)
            except:
                result = ''
        while result.endswith('<br>'):
            result = result[:-4]
        return result


    def __get_voice_duration(self, speaker_uuid: str, handle: str) -> str:
        if speaker_uuid:
            try:
                if speaker_uuid not in self.__soundbanks:
                    sb = soundbank_object(self.__assets.files.get_soundbank_file(speaker_uuid))
                    self.__soundbanks[speaker_uuid] = sb
                return self.__soundbanks[speaker_uuid].get_duration(handle)
            except:
                pass
            try:
                if speaker_uuid in self.__mod_soundbanks:
                    return self.__mod_soundbanks[speaker_uuid].get_duration(handle)
            except:
                pass
            try:
                if speaker_uuid in self.__extra_soundbanks:
                    return self.__extra_soundbanks[speaker_uuid].get_duration(handle)
            except:
                pass
        return '-'


    def get_text_lines(
            self,
            speaker_uuid: str | None,
            node_uuid: str,
            texts_with_rules: list[et.Element[str]],
            padding: str,
            question: bool
    ) -> list[str]:
        if not texts_with_rules:
            return []
        result = [f'{padding}<ul class="voicelines">']
        for text_with_rules in texts_with_rules:
            tags = text_with_rules.findall('./children/node[@id="RuleGroup"]/children/node[@id="Rules"]/children/node[@id="Rule"]/children/node[@id="Tags"]/children/node[@id="Tag"]')
            tag_strings = list[tuple[str, str]]()
            for tag in tags:
                tag_uuid = get_bg3_attribute(tag, 'Object')
                try:
                    if tag_uuid is not None:
                        tag_name = self.__tags.get_tag(tag_uuid).name
                    else:
                        tag_name = 'UNKNOWN_TAG'
                        tag_uuid = 'UNKNOWN_TAG'
                except:
                    tag_name = 'UNKNOWN_TAG'
                    tag_uuid = 'UNKNOWN_TAG'
                tag_strings.append((f'[{tag_name}]', tag_uuid))
            texts = text_with_rules.findall('./children/node[@id="TagTexts"]/children/node[@id="TagText"]')
            for text in texts:
                text_version = ''
                handle = get_required_bg3_attribute(text, 'TagText', value_name = 'handle')
                if handle == '':
                    translated_string = 'emtpy text'
                    handle = 'empty text handle'
                    voice_duration = '-'
                else:
                    text_version = get_required_bg3_attribute(text, 'TagText', value_name = 'version')
                    translated_string = self.__get_translated_string(handle)
                    if translated_string and isinstance(speaker_uuid, str) and not question:
                        voice_duration = self.__get_voice_duration(speaker_uuid, handle)
                    else:
                        voice_duration = '-'

                    # build index only for non-modded dialogs
                    if translated_string:
                        if self.__relative_file_path and isinstance(speaker_uuid, str):
                            self.__node_index[handle] = (translated_string, speaker_uuid, self.__relative_file_path, node_uuid)
                    else:
                        translated_string = 'unknown text'

                result.append(f'{padding}{PAD}<li class="voiceline" >')
                for ts in tag_strings:
                    tag_string = ts[0]
                    tag_uuid = ts[1]
                    result.append(f'{padding}{PAD}{PAD}<label class="clipboard" onclick="navigator.clipboard.writeText(\'{tag_uuid}\')">{tag_string}</label>')
                    result.append(f'{padding}{PAD}{PAD}<label> | </label>')
                result.append(f'{padding}{PAD}{PAD}<label class="clipboard" onclick="navigator.clipboard.writeText(atob(\'{b64encode(translated_string.encode()).decode()}\'))">{translated_string}</label>')
                result.append(f'{padding}{PAD}{PAD}<label> | </label>')
                result.append(f'{padding}{PAD}{PAD}<label class="clipboard" onclick="navigator.clipboard.writeText(\'{handle}\')"><i>{handle}</i></label>')
                if text_version:
                    result.append(f'{padding}{PAD}{PAD}<label> (version {text_version})</label>')
                result.append(f'{padding}{PAD}{PAD}<label> | </label>')
                result.append(f'{padding}{PAD}{PAD}<label class="clipboard" onclick="navigator.clipboard.writeText(\'{voice_duration}\')">{voice_duration}</label>')
                result.append(f'{padding}{PAD}</li>')

        result.append(f'{padding}</ul>')
        return result


    def get_flag_group_lines(self, d: dialog_object, flag_group: et.Element[str], setflags: bool, padding: str) -> list[str]:
        group_type = get_required_bg3_attribute(flag_group, 'type')
        flag_kw1 = 'Set' if setflags else 'Check'
        flag_kw2 = 'to' if setflags else 'is'
        result = [
            f'{padding}<li class="flaggroup" name="{group_type}">{flag_kw1} "{group_type}" flag(s):',
            f'{padding}{PAD}<ul>',
        ]
        flags = flag_group.findall('./children/node[@id="flag"]')
        for flag in flags:
            flag_uuid = get_required_bg3_attribute(flag, 'UUID')
            flag_value = get_required_bg3_attribute(flag, 'value')
            speaker_index = get_bg3_attribute(flag, 'paramval')
            extra_context = ''
            if group_type == 'Tag':
                try:
                    tag = self.__tags.get_tag(flag_uuid)
                    flag_name = tag.name
                except:
                    flag_name = f'UNKNOWN'
            elif group_type == 'Quest':
                try:
                    qs = self.__journal.get_quest_step(flag_uuid)
                    quest_title = self.__textbank.get_line(qs.quest_title) if qs.quest_title else ''
                    description = self.__textbank.get_line(qs.description) if qs.description else ''
                    flag_name = f'{qs.objective}'
                    extra_context = f', quest {qs.quest_id} "{quest_title}", objective {qs.objective} "{description}"'
                except:
                    flag_name = 'QuestStep'
            elif group_type == 'Script':
                try:
                    flag_obj = self.__flags.get_flag(flag_uuid)
                    flag_name = flag_obj.name
                    extra_context = f', {flag_obj.description}'
                except:
                    flag_name = f'UNKNOWN'
                    extra_context = ''
            else:
                try:
                    flag_name = self.__flags.get_flag(flag_uuid).name
                except:
                    flag_name = f'UNKNOWN'


            if speaker_index is not None:
                speaker_name = self.get_speaker_name_by_slot_index(d, speaker_index)
                result.append(f'{padding}{PAD}{PAD}<li class="notext" name="{flag_uuid}_{speaker_index}_{speaker_name}" >')
                result.append(f'{padding}{PAD}{PAD}{PAD}<label class="flag clipboard" onclick="navigator.clipboard.writeText(\'{flag_name}_{flag_uuid}\')">{flag_name}_</label>')
                result.append(f'{padding}{PAD}{PAD}{PAD}<label class="flag clipboard" onclick="navigator.clipboard.writeText(\'{flag_uuid}\')">{flag_uuid}</label>')
                result.append(f'{padding}{PAD}{PAD}{PAD}<label class="flag">&nbsp;{flag_kw2} {flag_value} on {speaker_name} (speaker {speaker_index}){extra_context}</label>')
                result.append(f'{padding}{PAD}{PAD}</li>')
            else:
                result.append(f'{padding}{PAD}{PAD}<li class="notext" name="{flag_uuid}" >')
                result.append(f'{padding}{PAD}{PAD}{PAD}<label class="flag clipboard" onclick="navigator.clipboard.writeText(\'{flag_name}_{flag_uuid}\')">{flag_name}_</label>')
                result.append(f'{padding}{PAD}{PAD}{PAD}<label class="flag clipboard" onclick="navigator.clipboard.writeText(\'{flag_uuid}\')">{flag_uuid}</label>')
                result.append(f'{padding}{PAD}{PAD}{PAD}<label class="flag">&nbsp;{flag_kw2} {flag_value}{extra_context}</label>')
                result.append(f'{padding}{PAD}{PAD}</li>')
        result.append(f'{padding}{PAD}</ul>')
        result.append(f'{padding}</li>')
        return result


    def retrieve_dialog_synopsis(self, e: dict[str, str]) -> list[str]:
        if 'lsj_path' in e:
            lsj_path = e['lsj_path']
            pak = self.__assets.index.get_pak_by_file(lsj_path)
            gf = game_file(self.__assets.tool, lsj_path, pak_name = pak)
        elif 'lsf_path' in e:
            lsf_path = e['lsf_path']
            pak = self.__assets.index.get_pak_by_file(lsf_path)
            gf = game_file(self.__assets.tool, lsf_path, pak_name = pak)
        else:
            raise RuntimeError(f'cannot retrieve dialog synopsis, e = {e}')

        editor_data = gf.root_node.find('./region[@id="editorData"]/node[@id="editorData"]')
        result = []
        if editor_data is not None:
            synopsis = get_bg3_attribute(editor_data, 'synopsis')
            how_to_trigger = get_bg3_attribute(editor_data, 'HowToTrigger')
            if synopsis:
                result.append('Synopsis: ' + synopsis)
            if how_to_trigger:
                result.append('How to trigger: ' + how_to_trigger)
        speakers = gf.root_node.findall('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="speakerlist"]/children/node[@id="speaker"]')
        speaker_slots = list[str]()
        for speaker in speakers:
            speaker_index = get_required_bg3_attribute(speaker, 'index')
            speaker_uuid = get_bg3_attribute(speaker, 'list')
            if speaker_uuid:
                speaker_name = self.__assets.index.get_character_name(speaker_uuid)
            else:
                speaker_name = 'unknown speaker'
            speaker_slots.append(f'Speaker {speaker_index}: {speaker_name}')
        result.append(' | '.join(speaker_slots))
        return result


    def is_party_banter(self, e: dict[str, str]) -> bool:
        if e['lsj_path']:
            p = e['lsj_path'].lower()
        elif e['lsf_path']:
            p = e['lsf_path'].lower()
        else:
            raise RuntimeError(f'entry has no paths: {e}')
        return 'party_banter' in p or '/pb_' in p


    def is_voice_bark(self, e: dict[str, str]) -> bool:
        if e['lsj_path']:
            p = e['lsj_path'].lower()
        elif e['lsf_path']:
            p = e['lsf_path'].lower()
        else:
            raise RuntimeError(f'entry has no paths: {e}')
        return '_pad_' in p \
            or '_ad_' in p \
            or '_vb_' in p \
            or '_pad.ls' in p \
            or '_ad.ls' in p \
            or '_vb.ls' in p


    def convert_dialog_to_html(self, dialog_name: str) -> None:
        d = self.__assets.get_dialog_object(dialog_name, with_editor_context = False)
        try:
            d_editor_ctx = self.__assets.get_dialog_object(dialog_name, with_editor_context = True)
        except:
            d_editor_ctx = d
        t = self.__assets.get_timeline_object(dialog_name)
        root_path = os.path.join(self.__assets.tool.env.env_root_path, 'dialog_parser')

        e = self.__assets.index.get_entry(dialog_name)
        
        if 'lsj_path' in e and e['lsj_path']:
            pos = e['lsj_path'].rfind('/')
            file_name = e['lsj_path'][pos + 1: -4] + '.html'

            path_pos = e['lsj_path'].find('/Story/Dialogs/')
            dirs = e['lsj_path'][path_pos + 15: pos].split('/')
        elif 'lsf_path' in e and e['lsf_path']:
            pos = e['lsf_path'].rfind('/')
            file_name = e['lsf_path'][pos + 1: -4] + '.html'

            path_pos = e['lsf_path'].find('/Story/DialogsBinary/')
            dirs = e['lsf_path'][path_pos + 21: pos].split('/')
        else:
            raise RuntimeError(f'entry has no paths: {e}')

        self.__root_dir_path = os.path.join('.', *(['..'] * len(dirs)))

        if self.is_party_banter(e):
            output_file_path = os.path.join(root_path, 'banters', *dirs, file_name)
            relative_file_path = os.path.join('.', 'banters', *dirs, file_name)
            index_file_path = os.path.join(root_path, 'index', 'banters', file_name.replace('.html', '.json'))
        elif self.is_voice_bark(e):
            output_file_path = os.path.join(root_path, 'voicebarks', *dirs, file_name)
            relative_file_path = os.path.join('.', 'voicebarks', *dirs, file_name)
            index_file_path = os.path.join(root_path, 'index', 'voicebarks', file_name.replace('.html', '.json'))
        else:
            output_file_path = os.path.join(root_path, 'dialogs', *dirs, file_name)
            relative_file_path = os.path.join('.', 'dialogs', *dirs, file_name)
            index_file_path = os.path.join(root_path, 'index', 'dialogs', file_name.replace('.html', '.json'))
        output_dir_path = os.path.dirname(output_file_path)
        index_dir_path = os.path.dirname(index_file_path)
        os.makedirs(output_dir_path, exist_ok = True)
        os.makedirs(index_dir_path, exist_ok = True)

        synopsis_lines = self.retrieve_dialog_synopsis(e)

        self.__relative_file_path = relative_file_path
        self.__internal_convert_dialog_file_to_html(output_file_path, index_file_path, d, d_editor_ctx, t, e, synopsis_lines)


    def convert_dialogs_to_html(self) -> None:
        log_file = os.path.join(self.__assets.tool.env.env_root_path, 'dialog_parser.log')
        with open(log_file, 'wt', encoding='utf-8', errors='replace') as log_file:
            all_names = self.__assets.index.get_all_dialog_names()
            processed = 0
            for dialog_name in all_names:
                processed += 1
                try:
                    t = time.time()
                    print_and_write(log_file, f'{datetime.datetime.now().astimezone()} Converting {processed} / {len(all_names)}: {dialog_name}')
                    if self.dialog_filter(dialog_name):
                        self.convert_dialog_to_html(dialog_name)
                        print_and_write(log_file, f'{datetime.datetime.now().astimezone()} Converted {processed} / {len(all_names)}: {dialog_name}; time elapsed {time.time() - t}')
                    else:
                        print_and_write(log_file, f'{datetime.datetime.now().astimezone()} Skipped: {dialog_name}; time elapsed {time.time() - t}')
                except:
                    t, ex, tb = sys.exc_info()
                    print_and_write(log_file, f'{datetime.datetime.now().astimezone()} Failed to convert {dialog_name}')
                    print_and_write(log_file, traceback.format_exception(t, ex, tb))
                log_file.flush()


    def dialog_filter(self, dialog_name: str) -> bool:
        e = self.__assets.index.get_entry(dialog_name)
        if 'CombatCinematics' in e['dialog_bank_path']:
            return False
        if '/Crimes/' in e['lsj_path'] \
                or '/NO_RECORD/' in e['lsj_path'] \
                or '_PointNClick_' in e['lsj_path']:
            return False
        return True


    def convert_dialogs_to_html_mp(self, /, parallelism: int | None = None) -> None:
        mp.set_start_method('spawn', force = True)
        log_file = os.path.join(self.__assets.tool.env.env_root_path, 'dialog_parser_mp_main.log')
        with open(log_file, 'wt', encoding='utf-8', errors='replace') as log_file:
            all_names = [n for n in self.__assets.index.get_all_dialog_names() if self.dialog_filter(n)]
            cpu_count = parallelism if parallelism is not None else os.cpu_count()
            if cpu_count is None:
                print_and_write(log_file, f'{datetime.datetime.now().astimezone()} failed to determine the number of available CPU cores, falling back to single threaded mode')
                self.convert_dialogs_to_html()
                return
            parts = list[tuple[dialog_to_html, list[str]]]()
            print_and_write(log_file, f'{datetime.datetime.now().astimezone()} running in a pool of {cpu_count} processes')
            for i in range(0, cpu_count):
                part = (dialog_to_html(self.__assets), list[str]())
                parts.append(part)
                print_and_write(log_file, f'{datetime.datetime.now().astimezone()} created part {i + 1}')
                log_file.flush()
            print_and_write(log_file, f'{datetime.datetime.now().astimezone()} adding dialog names to parts')
            for i in range(0, len(all_names)):
                parts[i % cpu_count][1].append(all_names[i])
            print_and_write(log_file, f'{datetime.datetime.now().astimezone()} waiting for results...')
            log_file.flush()
            mp_results = mp.Pool(processes = cpu_count).map(convert_dialogs_to_html_mp, parts)
            print_and_write(log_file, f'{datetime.datetime.now().astimezone()} got {len(mp_results)} results')
            failed_dialogs = list[str]()
            for mp_result in mp_results:
                for line in mp_result:
                    if 'failed to convert' in line:
                        failed_dialogs.append(line)
                    else:
                        print_and_write(log_file, f'{datetime.datetime.now().astimezone()} {line}')
            for line in failed_dialogs:
                print_and_write(log_file, f'{datetime.datetime.now().astimezone()} {line}')
            print_and_write(log_file, f'{datetime.datetime.now().astimezone()} finished')
            log_file.flush()


    def __write_index_file_header(self, f: io.TextIOWrapper, title: str) -> None:
        f.write("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>""" + title + """ voice lines index</title>
        <style>
            body {
                background-color: lightgrey;
                font-family: monospace;
                font-size: medium;
            }
            .file {
                background-color: white;
                width: auto;
                height: 100%;
                padding: 8px 0px 8px 8px;
                margin: 8px 0px 8px 8px;
                border: thin dotted;
            }
            .voiceline {
                margin: 8px 0px 8px 8px;
            }
            .visible {
                display: block;
            }
            .invisible {
                display: none;
            }
            .pointer {
                cursor: pointer;
            }
        </style>
    </head>
    <body>
""")


    def __write_file_header(self, f: io.TextIOWrapper, file_type: str, file_name: str) -> None:
        if file_type == 'dialogs':
            file_type_name = 'Dialog'
        elif file_type == 'banters':
            file_type_name = 'Party Banter'
        elif file_type == 'voicebarks':
            file_type_name = 'Automated Dialog/Voicebark'
        else:
            file_type_name = 'File'
        f.write(f"""
        <div class="file">
            <div><label>{file_type_name}: {file_name}</label></div>
""")


    def build_index_file(self, speakers: set[str]) -> None:
        root_path = os.path.join(self.__assets.tool.env.env_root_path, 'dialog_parser')
        index_files = dict[str, io.TextIOWrapper]()
        try:
            for speaker_uuid in speakers:
                speaker_name = self.__assets.index.get_character_name(speaker_uuid)
                if speaker_name:
                    f = open(os.path.join(root_path, f'{speaker_name}.html'), 'wt', encoding='utf-8', errors='replace')
                    index_files[speaker_uuid] = f
                    self.__write_index_file_header(f, speaker_name)
            for dialog_type in ['dialogs', 'banters', 'voicebarks']:
                index_dir_path = os.path.join(root_path, 'index', dialog_type)
                if not os.path.isdir(index_dir_path):
                    continue
                with os.scandir(index_dir_path) as fs_entries:
                    for e in fs_entries:
                        if e.is_file():
                            written_speakers = set[str]()
                            with open(e.path, 'rt', encoding='utf-8', errors='replace') as f:
                                filename = e.name
                                jo = json.load(f)
                                if not isinstance(jo, dict):
                                    raise TypeError(f'expected dict, got {type(jo)}')
                                for k, v in jo.items():
                                    if not isinstance(k, str):
                                        raise TypeError(f'expected str, got {type(k)}')
                                    if not isinstance(v, list):
                                        raise TypeError(f'expected list, got {type(v)}')
                                    text_handle = k
                                    translated_string, speaker_uuid, relative_file_path, node_uuid = v
                                    if speaker_uuid == 'NARRATOR':
                                        speaker_uuid = SPEAKER_NARRATOR
                                    if speaker_uuid in index_files:
                                        if speaker_uuid not in written_speakers:
                                            self.__write_file_header(index_files[speaker_uuid], dialog_type, filename)
                                            written_speakers.add(speaker_uuid)
                                        index_files[speaker_uuid].write(f"""
            <div class="voiceline">
                <a href="{relative_file_path}#{node_uuid}"><i>{text_handle}</i></a><label>&nbsp;->&nbsp;{translated_string}</label>
            </div>
""")
                                for written_speaker in written_speakers:
                                    index_files[written_speaker].write("""
        </div>
""")                                    
        finally:
            for f in index_files.values():
                f.write("""
    </body>
</html>
""")
                f.close()


    def convert_modded_dialog_to_html(self, mod_name: str, dialog_file: game_file, timeline_file: game_file | None) -> None:
        d = dialog_object(dialog_file)
        if timeline_file is not None:
            t = timeline_object(timeline_file, d)
        else:
            t = None
        root_path = os.path.join(self.__assets.tool.env.env_root_path, 'dialog_parser_' + mod_name)

        fn = dialog_file.relative_file_path
        e = {
            'lsf_path': fn,
        }
        
        pos = fn.rfind('/')
        file_name = fn[pos + 1: -4] + '.html'
        path_pos = fn.find('/Story/DialogsBinary/')
        dirs = fn[path_pos + 21: pos].split('/')

        self.__root_dir_path = os.path.join('.', *(['..'] * len(dirs)))

        output_file_path = os.path.join(root_path, *dirs, file_name)
        output_dir_path = os.path.dirname(output_file_path)
        os.makedirs(output_dir_path, exist_ok = True)

        speakers = dialog_file.root_node.findall('./region[@id="dialog"]/node[@id="dialog"]/children/node[@id="speakerlist"]/children/node[@id="speaker"]')
        speaker_slots = list[str]()
        for speaker in speakers:
            speaker_index = get_required_bg3_attribute(speaker, 'index')
            speaker_uuid = get_bg3_attribute(speaker, 'list')
            if speaker_uuid:
                speaker_name = self.__assets.index.get_character_name(speaker_uuid)
            else:
                speaker_name = 'unknown speaker'
            speaker_slots.append(f'Speaker {speaker_index}: {speaker_name}')

        synopsis_lines = [' | '.join(speaker_slots)]

        self.__relative_file_path = ''
        self.__internal_convert_dialog_file_to_html(output_file_path, '', d, None, t, e, synopsis_lines)


    def __internal_convert_dialog_file_to_html(
            self,
            output_file_path: str,
            index_file_path: str,
            dialog: dialog_object,
            dialog_with_context: dialog_object | None,
            timeline: timeline_object | None,
            dialog_entry: dict[str, str],
            synopsis_lines: list[str]
    ) -> None:
        sys.setrecursionlimit(10000)
        root_uuids = dialog.get_root_nodes()
        all_nodes_uuids = set[str]()
        for node in dialog.get_dialog_nodes():
            all_nodes_uuids.add(get_required_bg3_attribute(node, 'UUID'))

        self.__known_nodes.clear()
        self.__referenced_nodes.clear()
        self.__node_index.clear()

        for node_uuid in all_nodes_uuids:
            node = dialog.find_dialog_node(node_uuid)
            children = node.findall('./children/node[@id="children"]/children/node[@id="child"]')
            for child in children:
                child_node_uuid = get_required_bg3_attribute(child, 'UUID')
                if child_node_uuid in self.__referenced_nodes:
                    self.__referenced_nodes[child_node_uuid] += 1
                else:
                    self.__referenced_nodes[child_node_uuid] = 1

        with open(output_file_path, 'wt', encoding='utf-8', errors='replace') as f:
            self.start_dialog_html_file(dialog, dialog_entry, f, synopsis_lines)
            for node_uuid in root_uuids:
                self.convert_dialog_node_to_html(dialog, dialog_with_context, timeline, node_uuid, '', True, f, f'{PAD}{PAD}')            
            for node_uuid in all_nodes_uuids:
                if node_uuid not in self.__known_nodes and node_uuid not in self.__referenced_nodes:
                    self.convert_dialog_node_to_html(dialog, dialog_with_context, timeline, node_uuid, '', True, f, f'{PAD}{PAD}', is_orphan = True)
            self.finish_dialog_html_file(f)
        if index_file_path:
            with open(index_file_path, 'wt', encoding='utf-8', errors='replace') as f:
                json.dump(self.__node_index, f)


    def convert_modded_dialogs_to_html(self, pak_file_path: str, /, dialog_names: list[str] = [], extra_pak_path: str | None = None) -> None:
        if not os.path.isfile(pak_file_path):
            raise RuntimeError(f'mod pak not found: {pak_file_path}')
        if not pak_file_path.endswith('.pak'):
            raise RuntimeError(f'mod file is not a pak: {pak_file_path}')
        self.__extra_textbank = None
        self.__mod_textbank = None
        pak_fn = os.path.basename(pak_file_path)
        pos = pak_fn.find('_')
        if pos == -1:
            mod_name = pak_fn[:-4]
        else:
            mod_name = pak_fn[: pos]
        include_only_these = frozenset[str]([n.strip().lower() for n in dialog_names])

        log_file = os.path.join(self.__assets.tool.env.env_root_path, f'dialog_parser_{os.path.basename(pak_file_path)}.log')
        with open(log_file, 'wt', encoding='utf-8', errors='replace') as log_file:
            self.__flags.add_flags_to_registry(pak_file_path)
            self.__tags.add_tags_to_registry(pak_file_path)

            mod_files = self.__assets.files.tool.list(pak_file_path)
            try:
                processed = 0

                if extra_pak_path:
                    self.__flags.add_flags_to_registry(extra_pak_path)
                    self.__tags.add_tags_to_registry(extra_pak_path)
                    extra_pak_files = self.__assets.files.tool.list(extra_pak_path)
                    for fn in extra_pak_files:
                        if 'Localization/English/' in fn and fn.endswith('.loca'):
                            print_and_write(log_file, f'{datetime.datetime.now().astimezone()} found extra textbank: {fn}')
                            self.__extra_textbank = loca_object(game_file(self.__assets.tool, fn, pak_name = extra_pak_path))
                        if '/Localization/English/Soundbanks/' in fn and fn.endswith('.lsf'):
                            print_and_write(log_file, f'{datetime.datetime.now().astimezone()} found extra soundbank: {fn}')
                            sb = soundbank_object(game_file(self.__assets.tool, fn, pak_name = extra_pak_path))
                            self.__extra_soundbanks[sb.speaker_id] = sb

                dialogs = list[str]()
                timelines = dict[str, str]()
                for fn in mod_files:
                    if 'Localization/English/' in fn and fn.endswith('.loca'):
                        print_and_write(log_file, f'{datetime.datetime.now().astimezone()} found mod textbank: {fn}')
                        self.__mod_textbank = loca_object(game_file(self.__assets.tool, fn, pak_name = pak_file_path))
                    elif '/Story/DialogsBinary/' in fn and fn.endswith('.lsf'):
                        dialogs.append(fn)
                    elif '/Timeline/Generated/' in fn and fn.endswith('.lsf'):
                        timeline_key, _ = os.path.splitext(os.path.basename(fn))
                        timelines[timeline_key.lower()] = fn
                    elif '/Localization/English/Soundbanks/' in fn and fn.endswith('.lsf'):
                        print_and_write(log_file, f'{datetime.datetime.now().astimezone()} found mod soundbank: {fn}')
                        sb = soundbank_object(game_file(self.__assets.tool, fn, pak_name = pak_file_path))
                        self.__mod_soundbanks[sb.speaker_id] = sb

                for dialog in dialogs:
                    dialog_file_name = os.path.basename(dialog)
                    dialog_name, _ = os.path.splitext(dialog_file_name)
                    dialog_name = dialog_name.lower()
                    processed += 1
                    if include_only_these and dialog_name not in include_only_these:
                        print_and_write(log_file, f'{datetime.datetime.now().astimezone()} Skipping {processed} / {len(dialogs)}: {dialog_file_name}')
                        continue
                    t = time.time()
                    print_and_write(log_file, f'{datetime.datetime.now().astimezone()} Converting {processed} / {len(dialogs)}: {dialog_file_name}')
                    if dialog_name in timelines:
                        timeline_gf = game_file(self.__assets.files.tool, timelines[dialog_name], pak_name = pak_file_path)
                    else:
                        timeline_gf = None
                    dialog_gf = game_file(self.__assets.files.tool, dialog, pak_name = pak_file_path)
                    self.convert_modded_dialog_to_html(mod_name, dialog_gf, timeline_gf)
                    print_and_write(log_file, f'{datetime.datetime.now().astimezone()} Converted {processed} / {len(dialogs)}: {dialog_file_name}; time elapsed {time.time() - t}')

            finally:
                self.__mod_textbank = None
                self.__extra_textbank = None


def convert_dialogs_to_html_mp(args: tuple[object, ...]) -> list[str]:
    pid = os.getpid()
    if len(args) != 2:
        return [f'[{pid}] expected 2 arguments, got {len(args)}']
    dth = args[0]
    dialog_names = args[1]
    if not isinstance(dth, dialog_to_html):
        return [f'[{pid}] expected dialog_to_html as the 1st argument, got {type(dth)}']
    if not isinstance(dialog_names, list):
        return [f'[{pid}] expected list as the 2nd argument, got {type(dialog_names)}']
    result = list[str]()
    log_file = os.path.join(dth.assets.tool.env.env_root_path, f'dialog_parser_mp_{os.getpid()}.log')
    processed = 1
    total = len(dialog_names)
    gt = time.time()
    failed_dialogs = []
    with open(log_file, 'wt', encoding='utf-8', errors='replace') as log_file:
        for dialog_name in dialog_names:
            try:
                if not isinstance(dialog_name, str):
                    msg = f'[{pid}]  expected str list element, got {type(dialog_name)}'
                    print_and_write(log_file, f'{datetime.datetime.now().astimezone()} {msg}')
                    return [msg]
                t = time.time()
                dth.convert_dialog_to_html(dialog_name)
                t = time.time() - t
                msg = f'[{pid}] [{processed}/{total}] converted {dialog_name} in {t} seconds'
                result.append(msg)
                print_and_write(log_file, f'{datetime.datetime.now().astimezone()} {msg}')
            except:
                failed_dialogs.append(dialog_name)
                msg = f'[{pid}] [{processed}/{total}] failed to convert {dialog_name}'
                result.append(msg)
                print_and_write(log_file, f'{datetime.datetime.now().astimezone()} {msg}')
                t, ex, tb = sys.exc_info()
                print_and_write(log_file, traceback.format_exception(t, ex, tb))
            processed += 1
            log_file.flush()
        gt = time.time() - gt
        print_and_write(log_file, f'[{pid}] completed conversion of {processed} dialogs in {gt} seconds, number of failures {len(failed_dialogs)}')
        for failed_dialog in failed_dialogs:
            print_and_write(log_file, f'[{pid}] failed to convert: {failed_dialog}')
    return result
