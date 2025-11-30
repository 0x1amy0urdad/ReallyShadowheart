from __future__ import annotations

import gzip
import json
import os.path
import sys
import xml.etree.ElementTree as et

from ._files import game_files

# Origins and Companions: speaker uuids; these are global templates UUIDs and used in dialogs to refer to speakers
SPEAKER_SHADOWHEART = '3ed74f06-3c60-42dc-83f6-f034cb47c679'
SPEAKER_MINSC       = '0de603c5-42e2-4811-9dad-f652de080eba'
SPEAKER_MINTHARA    = '25721313-0c15-4935-8176-9f134385451b'
SPEAKER_KARLACH     = '2c76687d-93a2-477b-8b18-8a14b549304c'
SPEAKER_LAEZEL      = '58a69333-40bf-8358-1d17-fff240d7fb12'
SPEAKER_HALSIN      = '7628bc0e-52b8-42a7-856a-13a6fd413323'
SPEAKER_JAHEIRA     = '91b6b200-7d00-4d62-8dc9-99e8339dfa1a'
SPEAKER_GALE        = 'ad9af97d-75da-406a-ae13-7071c563f604'
SPEAKER_WYLL        = 'c774d764-4a17-48dc-b470-32ace9ce447d'
SPEAKER_ASTARION    = 'c7c13742-bacd-460a-8f65-f864fe41f255'
SPEAKER_DURGE       = 'e6b3c2c4-e88d-e9e6-ffa1-d49cdfadd411'
SPEAKER_NIGHTSONG   = '6c55edb0-901b-4ba4-b9e8-3475a8392d9b'
SPEAKER_ISOBEL      = '263bfbfc-6160-46f4-a9e1-1089cdb5c211'
SPEAKER_BOO         = 'd49e3b49-a089-4465-b453-28dc79e82bb3'
SPEAKER_MIZORA      = '491a7686-3081-405b-983c-289ec8781e0a'
SPEAKER_VICONIA     = 'b1ea974d-96fb-47ca-b6d9-9c85fcb69313'
SPEAKER_ARNELL      = 'c12d561f-beae-4ef6-917e-0bec2f829449'
SPEAKER_EMMELINE    = 'd085272a-f1d0-4ff8-a498-80728030f83e'
SPEAKER_NYM_ORLYTH  = '7574fc5a-3645-4370-a778-0b38d0ef162a'
SPEAKER_SORN_ORLYTH = 'f25b5f9a-bfde-4d81-a3fb-74fc39dad95b'
SPEAKER_GANDREL     = '0e47fcb9-c0c4-4b0c-902b-2d13d209e760'
SPEAKER_JERGAL      = '0133f2ad-e121-4590-b5f0-a79413919805'
SPEAKER_ZEVLOR      = '475200ee-cc3c-4dbe-84b1-1820c02ea26a'
SPEAKER_ARADIN      = '82d1b843-9e8c-48a5-9d87-caddea5c193c'
SPEAKER_HAARLEP     = '1867db0b-748c-94ae-c4f0-69cfd306c180'
SPEAKER_SCELERITAS  = 'f3486165-268f-4e41-9e0c-51485dfdff10'
SPEAKER_PLAYER      = 'e0d1ff71-04a8-4340-ae64-9684d846eb83'
SPEAKER_NARRATOR    = 'a346318f-15b3-49ad-ab97-ddf8283dc339'

SPEAKER_NAME = {
    SPEAKER_PLAYER      : 'Player',
    SPEAKER_SHADOWHEART : 'Shadowheart',
    SPEAKER_ARNELL      : 'Arnell Hallowleaf',
    SPEAKER_EMMELINE    : 'Emmeline Hallowleaf',
    SPEAKER_NARRATOR    : 'Narrator',
    SPEAKER_MINSC       : 'Minsc',
    SPEAKER_MINTHARA    : 'Minthara',
    SPEAKER_KARLACH     : 'Karlach',
    SPEAKER_LAEZEL      : 'Lae\'zel',
    SPEAKER_HALSIN      : 'Halsin',
    SPEAKER_JAHEIRA     : 'Jaheira',
    SPEAKER_GALE        : 'Gale',
    SPEAKER_WYLL        : 'Wyll',
    SPEAKER_ASTARION    : 'Astarion',
    SPEAKER_DURGE       : 'Durge',
    SPEAKER_NIGHTSONG   : 'Nightsong',
    SPEAKER_ISOBEL      : 'Isobel',
    SPEAKER_BOO         : 'Boo',
    SPEAKER_MIZORA      : 'Mizora',
    SPEAKER_VICONIA     : 'Viconia DeVir',
    SPEAKER_NYM_ORLYTH  : 'Nym Orlyth',
    SPEAKER_SORN_ORLYTH : 'Sorn Orlyth',
    SPEAKER_GANDREL     : 'Gandrel',
    SPEAKER_JERGAL      : 'Jergal',
    SPEAKER_HAARLEP     : 'Haarlep',
    SPEAKER_SCELERITAS  : 'Sceleritas Fel'
}
