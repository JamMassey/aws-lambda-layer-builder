from __future__ import annotations

import logging

## There is a Docker SDK for Python that we could use. As for now I'm just using subprocess.run to run the docker commands, at least it saves having to rely on an extra dependency.
import subprocess
from typing import TYPE_CHECKING

logger = logging.getLogger(__name__)
if TYPE_CHECKING:
    from typing import Dict, List


def build_and_run_docker_image(
    dockerfile_path: str,
    image_name: str,
    env_variables: Dict = {},
    build_args: Dict = {},
    remove_container: bool = False,
    prevent_background_exit: bool = False,
    publish_all_ports: bool = False,
    volumes: List = [],
    detach: bool = False,
    interactive: bool = False,
    cache: bool = False,
    **kwargs,
):
    cmd = ["docker", "build", "-t", image_name, "-f", dockerfile_path, "."]
    if not cache:
        cmd += ["--no-cache"]
    for key, value in build_args.items():
        cmd.extend(["--build-arg", f"{key}={value}"])
    subprocess.run(cmd)
    cmd = ["docker", "run"]
    if remove_container:
        cmd += ["--rm"]
    if publish_all_ports:
        cmd += ["-P"]
    for volume in volumes:
        cmd += ["-v", volume]
    if prevent_background_exit:
        cmd += ["-t"]
    if interactive:
        cmd += ["-it"]
    if detach:
        cmd += ["-d"]
    if kwargs:
        for key, value in kwargs.items():
            cmd += [key, value]
    cmd += [image_name]
    for key, value in env_variables.items():
        cmd += ["-e", f"{key}={value}"]
    subprocess.run(cmd)


def copy_file_from_container(container_name: str, src: str, dest: str):
    subprocess.run(["docker", "cp", f"{container_name}:{src}", dest])


def remove_container(container_name: str):
    subprocess.run(["docker", "rm", container_name])


def kill_container(container_name: str):
    subprocess.run(["docker", "kill", container_name])
