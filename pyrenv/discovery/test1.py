"""
    This module is meant to automatically
    find a Python venv, or ask the user to
    manually enter it.
"""

import os
from pathlib import Path

from typing import NoReturn, Any, List, Optional

POETRY_ENV_PATH_CMD: str = "poetry env info --path"


def discover_venv_path() -> Path:
    """get the virtual environmnent full POSIX path.
    This is automatically found via POETRY_ENV_PATH_CMD

    Caveats:
        If there is no pyproject.toml in the cwd, or in any
        any of its parents, _path_str will be an error
        message instead of a valid pathlib.Path object.

        This will also be the case if the file pyproject.toml
        is found but the virualenv has not been created.
        In this case you should run `poetry install` to create it.
    """
    cmd: str = POETRY_ENV_PATH_CMD
    # strip the path from the newline terminator :
    _path_str: str = os.popen(cmd).read().replace("\n", "")
    return Path(_path_str)

def prompt_validate_path(venv_path: Optional[Path] = None) -> Path:
    """ """
    venv_path: Path = venv_path or Path(".-.")
    assert isinstance(venv_path, Path), f"{venv_path} is not a valid Path"

    # Does venv_path exist ?
    while not venv_path.exists():
        _path_str = input("Please provide the absolute path to the vitual environment : ")
        venv_path = Path(_path_str)
    
    # Is it presumably a virtualenv ?
    py: bool = "py" in venv_path.absolute().as_posix()
    env: bool = "env" in venv_path.absolute().as_posix()
    if not (py and env):
        print(f"Path {venv_path.absolute()} does not appear to be a virtual environment")
        confirm = input("Continue ? [Y/n] ")
        if confirm == "Y":
            return venv_path
        else:
            return validate_path()
    else:
        return venv_path

def main():
    """ A simple test """
    _path = discover_venv_path()
    return prompt_validate_path(_path)


if __name__ == "__main__":
    main()
