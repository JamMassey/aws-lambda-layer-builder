from __future__ import annotations
## There is a Docker SDK for Python that we could use. As for now I'm just using subprocess.run to run the docker commands, at least it saves having to rely on an extra dependency.
import logging
from util.args_util import parse_args
from util.logging_util import setup_logger
from core.docker import build_and_run_docker_image, copy_file_from_container, remove_container
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict

logger = logging.getLogger(__name__)

# For now only supports one package and one container at a time. Package can be a requirement.txt file, a local path or a single package name. All dependant packages will also be installed.
def build_aws_lamda_layer(package: str, output_path: str, output_layer_name: str, local: bool, git_auth: Dict = None, runtime: str = "3.8") -> None:
    if local:
        target = package.split("/")[-1]
        if package.endswith(".txt"):
            target = "-r " + target
        build_and_run_docker_image(
            dockerfile_path="Dockerfiles/local_install.Dockerfile",
            image_name="lambda-layer-builder",
            build_args={"PATH_TO_LOCAL_FILE": package, "PACKAGE": target, "OUTPUT_NAME": output_layer_name, "RUNTIME": runtime},
            **{"--name": "lambda-layer-builder"}
        )
    elif git_auth: # Can maybe do some conditional logic within a RUN call within this Dockerfile and merge it with the single_pypi_package Dockerfile.
        build_and_run_docker_image(
            dockerfile_path="Dockerfiles/git_private_package.Dockerfile",
            image_name="lambda-layer-builder",
            build_args={"PACKAGE": package, "OUTPUT_NAME": output_layer_name, "RUNTIME": runtime, "GIT_USERNAME": git_auth["Username"], "GIT_PASSWORD": git_auth["Password"]},
            **{"--name": "lambda-layer-builder"}
        )
    else:
        build_and_run_docker_image(
            dockerfile_path="Dockerfiles/single_pypi_package.Dockerfile",
            image_name="lambda-layer-builder",
            build_args={"PACKAGE": package, "OUTPUT_NAME": output_layer_name, "RUNTIME": runtime},
            **{"--name": "lambda-layer-builder"}
        )
    copy_file_from_container("lambda-layer-builder", f"var/task/{output_layer_name}.zip", f"{output_path}/{output_layer_name}.zip")
    remove_container("lambda-layer-builder")


def main() -> None:
    args = parse_args()
    setup_logger(
        level=args.log_level,
        stream_logs=args.console_log,
    )
    logger.info("Logger initialised")
    if bool(args.git_username) != bool(args.git_password):
        raise ValueError("I attempting to authenticate for git you must provide both git username and password.")
    if args.runtime not in ["python3.9","python3.8", "python3.7", "python3.6"]:
        raise ValueError("Runtime must be one of 3.8, 3.7 or 3.6")
    if args.git_username and args.git_password:
        git_auth = {"Username": args.git_username, "Password": args.git_password}
    else:
        git_auth = None
    build_aws_lamda_layer(package=args.target_package, output_path=args.output_path, output_layer_name=args.output_layer_name, local=args.local, git_auth=git_auth, runtime=args.runtime)
    
if __name__ == "__main__":
	main()