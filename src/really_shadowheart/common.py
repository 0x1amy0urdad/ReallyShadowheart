from __future__ import annotations

import bg3moddinglib as bg3

from .flags import Really_Shadowheart_Softened_Version

def create_approval_fork(
    d: bg3.dialog_object,
    target_node_uuid: str,
    new_approval: bg3.reaction_object,
    skip_new_approval_global_flag_uuid: str | None = None
) -> str:
    if skip_new_approval_global_flag_uuid is None:
        skip_new_approval_global_flag_uuid = Really_Shadowheart_Softened_Version.uuid
    target_node = d.find_dialog_node(target_node_uuid)
    ori_approval_uuid = bg3.get_bg3_attribute(target_node, 'ApprovalRatingID')
    if ori_approval_uuid is not None:
        bg3.delete_bg3_attribute(target_node, 'ApprovalRatingID')
    result_node_uuid = bg3.new_random_uuid()
    new_approval_node_uuid = bg3.new_random_uuid()
    old_approval_node_uuid = bg3.new_random_uuid()
    d.create_standard_dialog_node(
        result_node_uuid,
        bg3.SPEAKER_PLAYER,
        [new_approval_node_uuid, old_approval_node_uuid],
        None)
    d.create_standard_dialog_node(
        new_approval_node_uuid,
        bg3.SPEAKER_PLAYER,
        [target_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(skip_new_approval_global_flag_uuid, False, None),
            )),
        ),
        approval_rating_uuid = new_approval.uuid)
    d.create_standard_dialog_node(
        old_approval_node_uuid,
        bg3.SPEAKER_PLAYER,
        [target_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(skip_new_approval_global_flag_uuid, True, None),
            )),
        ),
        approval_rating_uuid = ori_approval_uuid)
    return result_node_uuid
