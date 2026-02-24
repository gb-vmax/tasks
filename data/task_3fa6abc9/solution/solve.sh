#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Before starting the task, the /home/user directory exists and is writable by the user. No virtual environment named /home/user/diskmon-env exists yet.
# 
# On successful completion, the following should be true:
# 
# - A directory /home/user/diskmon-env is created.
# - The directory contains a Python virtual environment (created with python -m venv).
# - Within the activated environment, psutil version 5.9.8 and click version 8.1.7 are installed via pip.
# - Other packages commonly auto-installed or upgraded by venv and pip may appear: pip (specific version depending on venv/python version), setuptools, wheel, etc.
# - /home/user/diskmon-env/pip-freeze.log contains exact output of "pip freeze" after installation of the requested packages. At a minimum, it must have:
# psutil==5.9.8
# click==8.1.7
# plus (possibly):
# pip==
# setuptools==
# wheel==
# (these versions depend on Python/venv defaults in the environment).
# - The file /home/user/diskmon-env/pip-freeze.log has strict "package==version" pairs, one per line, with at least the two specified packages at their required versions present, matching pip freeze output from within the environment at runtime.

echo 'No automated solution provided.'
