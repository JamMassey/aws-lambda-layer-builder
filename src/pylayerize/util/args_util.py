#!/usr/bin/env python
from __future__ import annotations

import logging
from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from typing import OrderedDict

logger = logging.getLogger(__name__)


def add_boolean_arg(parser: ArgumentParser, name: str, desc: str, default: bool = False) -> None:
    """Adds a boolean arg to the arg parser allowing --arg and --no-arg for True and False respectively

    Parameters
    ----------
    parser : ArgumentParser
        Arg parser to add the argument to
    name : str
        Name of the argument
    desc : str
        Description of the arg to add
    default : bool, optional
        Default value of the boolean flag, by default False
    """
    dest = name.replace("-", "_")
    group = parser.add_argument_group(f"{name} options:", desc)
    me_group = group.add_mutually_exclusive_group(required=False)
    me_group.add_argument(f"--{name}", dest=dest, action="store_true", help="(default)" if default else "")
    me_group.add_argument(
        f"--no-{name}",
        dest=dest,
        action="store_false",
        help="(default)" if not default else "",
    )
    parser.set_defaults(**{dest: default})

@dataclass
class Args:
    """Data Class for storing CL args"""
    target_package: str
    output_path: Path = Path("./")
    output_layer_name: str = "lambda_layer"
    log_level: int = logging.INFO
    console_log: bool = True
    local: bool = False
    git_username: str = None
    git_password: str = None
    runtime: str = "python3.8"

def parse_args() -> Args:
    """Parses CL args into a Args object

    Returns
    -------
    Args
        Args object containing all the
    """
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-tp","--target-package", type=str, required=True, dest="target_package", help="The target package to build a layer for")
    arg_parser.add_argument("-op","--output-path", type=Path, dest="output_path", default = Path("./"), help="The output path for the layer .zip file")
    arg_parser.add_argument("-n","--output-layer-name", type=str, default="lambda_layer", dest="output_layer_name", help="The name of the output .zip file")
    arg_parser.add_argument(
        "-ll",
        "--log-level",
        default=logging.INFO,
        type=int,
        dest="log_level",
        help="The log level of logging",
    )
    arg_parser.add_argument("-gu", "--git-username", type=str, dest="git_username", help="The git username to use for the git clone")
    arg_parser.add_argument("-gp", "--git-password", type=str, dest="git_password", help="The git password to use for the git clone")
    arg_parser.add_argument("-rt", "--runtime", type=str, default="python3.8",dest="runtime", help="The runtime to use for the layer")
    add_boolean_arg(arg_parser, "console-log", "Log to console", default=True)
    add_boolean_arg(arg_parser, "local", "Set to True if you want to use a requirments.txt file or a custom lib stored locally.", default=False)

    return Args(**OrderedDict(vars(arg_parser.parse_args())))