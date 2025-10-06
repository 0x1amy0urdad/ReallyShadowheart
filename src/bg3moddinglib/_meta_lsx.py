from __future__ import annotations

def create_meta_lsx(
        mod_name: str,
        mod_display_name: str,
        description: str,
        mod_uuid: str,
        author: str,
        publish_handle: int,
        mod_version: tuple[int, int, int, int],
        pak_size: int,
        mod_hash: str
) -> str:
    version = mod_version[3] + (mod_version[2] << 31) + (mod_version[1] << 47) + (mod_version[0] << 55)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="8" revision="0" build="200"/>
    <region id="Config">
        <node id="root">
            <children>
                <node id="Conflicts"/>
                <node id="Dependencies">
                    <children>
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSString" value="GustavDev"/>
                            <attribute id="MD5" type="LSString" value="383c1ccdfd088fba5fb7bdce64c57a85"/>
                            <attribute id="Name" type="LSString" value="GustavDev"/>
                            <attribute id="PublishHandle" type="uint64" value="0"/>
                            <attribute id="UUID" type="guid" value="28ac9ce2-2aba-8cda-b3b5-6e922f71b6b8"/>
                            <attribute id="Version64" type="int64" value="145241302737902957"/>
                        </node>
                    </children>
                </node>
                <node id="ModuleInfo">
                    <attribute id="Author" type="LSString" value="{author}"/>
                    <attribute id="CharacterCreationLevelName" type="FixedString" value=""/>
                    <attribute id="Description" type="LSString" value="{description}"/>
                    <attribute id="FileSize" type="uint64" value="{pak_size}"/>
                    <attribute id="Folder" type="LSString" value="{mod_name}_{mod_uuid}"/>
                    <attribute id="LobbyLevelName" type="FixedString" value=""/>
                    <attribute id="MD5" type="LSString" value="{mod_hash}"/>
                    <attribute id="MenuLevelName" type="FixedString" value=""/>
                    <attribute id="Name" type="LSString" value="{mod_display_name}"/>
                    <attribute id="NumPlayers" type="uint8" value="4"/>
                    <attribute id="PhotoBooth" type="FixedString" value=""/>
                    <attribute id="PublishHandle" type="uint64" value="{publish_handle}"/>
                    <attribute id="StartupLevelName" type="FixedString" value=""/>
                    <attribute id="UUID" type="FixedString" value="{mod_uuid}"/>
                    <attribute id="Version64" type="int64" value="{version}"/>
                    <children>
                        <node id="PublishVersion">
                            <attribute id="Version64" type="int64" value="144255927717549775"/>
                        </node>
                        <node id="Scripts">
                            <children>
                                <node id="Script">
                                    <attribute id="UUID" type="FixedString" value="1953f77d-a201-45d7-a194-9b84c34b8461"/>
                                    <children>
                                        <node id="Parameters">
                                            <children>
                                                <node id="Parameter">
                                                    <attribute id="MapKey" type="FixedString" value="HardcoreOnly"/>
                                                    <attribute id="Type" type="int32" value="1"/>
                                                    <attribute id="Value" type="LSString" value="0"/>
                                                </node>
                                            </children>
                                        </node>
                                    </children>
                                </node>
                                <node id="Script">
                                    <attribute id="UUID" type="FixedString" value="0d6510f5-50a3-4ecd-83d8-134c9a640324"/>
                                    <children>
                                        <node id="Parameters">
                                            <children>
                                                <node id="Parameter">
                                                    <attribute id="MapKey" type="FixedString" value="HardcoreOnly"/>
                                                    <attribute id="Type" type="int32" value="1"/>
                                                    <attribute id="Value" type="LSString" value="0"/>
                                                </node>
                                            </children>
                                        </node>
                                    </children>
                                </node>
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
"""#.replace("\r\n", "\n")