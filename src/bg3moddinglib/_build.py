from __future__ import annotations

import sys

from ._assets import bg3_assets

from typing import Callable

PRE_BUILD_PROCEDURES = dict[int, list[tuple[str, Callable[[], None]]]]()
BUILD_PROCEDURES = list[tuple[str, Callable[[], None]]]()
PARAMETERS = dict[str, str]()

YES_TOKENS = frozenset(('yes', 'y', 'true', 't', '1'))

def add_pre_build_procedure(priority: int, proc_name: str, proc: Callable[[], None], feature_name: str | None = None, enabled: bool = True) -> None:
    if feature_name:
        if priority not in PRE_BUILD_PROCEDURES:
            PRE_BUILD_PROCEDURES[priority] = list[tuple[str, Callable[[], None]]]()
        PRE_BUILD_PROCEDURES[priority].append((proc_name, lambda: proc() if feature_enabled(feature_name, enabled) else None))
    else:
        if priority not in PRE_BUILD_PROCEDURES:
            PRE_BUILD_PROCEDURES[priority] = list[tuple[str, Callable[[], None]]]()
        PRE_BUILD_PROCEDURES[priority].append((proc_name, proc))

def add_build_procedure(proc_name: str, proc: Callable[[], None], feature_name: str | None = None, enabled: bool = True) -> None:
    if feature_name:
        BUILD_PROCEDURES.append((proc_name, lambda: proc() if feature_enabled(feature_name, enabled) else None))
    else:
        BUILD_PROCEDURES.append((proc_name, proc))

def set_parameters(params: dict[str, str]) -> None:
    global PARAMETERS
    for k, v in params.items():
        PARAMETERS[k] = v
        sys.stdout.write(f'parameter {k} = {v}\n')

def get_parameter(name: str) -> str | None:
    if name in PARAMETERS:
        return PARAMETERS[name]
    return None

def feature_enabled(name: str, enabled: bool = True, verbose = True) -> bool:
    if verbose:
        if enabled:
            sys.stdout.write(f", checking if feature '{name}' is enabled, it is ")
        else:
            sys.stdout.write(f", checking if feature '{name}' is disabled, it is ")
    if name in PARAMETERS:
        value = PARAMETERS[name].lower() in YES_TOKENS
        if value:
            if verbose:
                sys.stdout.write("enabled")
            return enabled
        if verbose:
            sys.stdout.write("disabled")
        return not enabled
    if verbose:
        sys.stdout.write("undefined")
    return False

def run_build_procedures(assets: bg3_assets | None = None) -> None:
    priorities = list[int](PRE_BUILD_PROCEDURES.keys())
    priorities.sort()
    for priority in priorities:
        for build_proc_name, build_proc_callable in PRE_BUILD_PROCEDURES[priority]:
            sys.stdout.write(f'Running pre-build procedure: {build_proc_name}')
            build_proc_callable()
            sys.stdout.write('\n')
    for build_proc_name, build_proc_callable in BUILD_PROCEDURES:
        sys.stdout.write(f'Running build procedure: {build_proc_name}')
        build_proc_callable()
        sys.stdout.write('\n')
    if assets is not None:
        assets.post_process_assets()
    sys.stdout.write('All build procedures are completed\n')
