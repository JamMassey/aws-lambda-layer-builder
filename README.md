# Pylayerize
Pylayerize simplifies the process of creating AWS Lambda Layers by leveraging Docker to compile and package Python dependencies for any targeted runtime. With support for custom packages and private GitHub repos, pylayerize optimizes the creation and deployment of Lambda Layers for improved development efficiency.

### General Usage
To use Pylayerize, you must first install it using pip:
```ruby
$ pip install pylayerize
```
Once pylayerize is installed, you can run it from the command line by invoking the pylayerize command.
```ruby
$ pylayerize -tp <target_package> [OPTIONS]
```

#### Required Options:

-tp, --target-package: The target package to build a layer for.

#### Optional Options:

1. -h, --help: Show the help message and exit.
2. -op, --output-path: The output path for the layer .zip file. Default is the current directory (.).
3. -n, --output-layer-name: The name of the output .zip file. Default is lambda_layer.
4. -ll, --log-level: The log level of logging. Default is INFO.
5. -gu, --git-username: The git username to use for the git clone.
6. -gp, --git-password: The git password to use for the git clone.
7. -rt, --runtime: The runtime to use for the layer. Default is python3.8.
8. --console-log, --no-console-log: Log to console. Default is True.
9. --local, --no-local: Set to True if you want to use a requirments.txt file or a custom lib stored locally. Default is False.

#### Examples
To build a layer for numpy using the default options, run:

```ruby
$ pylayerize -tp my_package
```

To build a layer for numpy with a custom output path and layer name, run:

```ruby
$ pylayerize -tp numpy -op /path/to/output -n my_layer
```

To build a layer for private GitHub repositories that require authentication, run:
```ruby
$ pylayerize --target-package git+my_repo_link --git-username my_username --git-password my_password
```

If you have a local requirements.txt file at /path/to/requirements.txt, you can use it by running

```ruby
$ pylayerize --target-package mypackage --local --requirements-file /path/to/requirements.txt
```

#### Programatic Usage

It is also possible to use pylayerize and its components programatically in Python.

```python
from pylayerize import build_aws_lamda_layer
```


### Contributions

Contributions are welcome! Here are some guidelines for contributing to this project:

Fork this repository and create a new branch for your feature or bug fix.
Make your changes and commit them with descriptive commit messages.
Create a pull request against the dev branch and describe your changes and the problem they solve.
Ensure that your code passes all tests and meets the project's code standards.
Respond to any feedback from maintainers and make any necessary changes.
If you'd like to contribute but aren't sure where to start, take a look at the project's issue tracker. Issues marked as "help wanted" or "good first issue" are a good place to start.


### Version Bumping through PR titles
Our repository uses an automated versioning system that relies on the naming convention of the pull request titles. When you merge a pull request into the dev branch, the version number of the project is automatically bumped and a new tag is created, based on the prefix in your PR title.

The version number follows the MAJOR.MINOR.FIX format, where:

MAJOR version increments indicate significant changes or enhancements in the project, often including breaking changes.
MINOR version increments indicate backwards-compatible new features or enhancements.
FIX version increments indicate backwards-compatible bug fixes or minor changes.
To specify the type of changes you have made in your pull request, prefix your PR title with one of the following:

major: - to increment the MAJOR version (e.g., from 1.0.0 to 2.0.0).
minor: - to increment the MINOR version (e.g., from 0.1.0 to 0.2.0).
fix: - to increment the FIX version (e.g., from 0.0.1 to 0.0.2).
For example, if you have made a minor change, your PR title could be: minor: Add new feature XYZ.

If your PR title does not include any of the specified prefixes, the GitHub Action will not increment the version or create a new tag. This can be useful for non-functional changes like updates to documentation or code refactoring that don't require a version bump.

When your PR is merged into main, the GitHub Action will increment the version according to the prefix in the PR title and create a new tag.

Please ensure you follow this convention to maintain a well-structured and meaningful version history for our project.