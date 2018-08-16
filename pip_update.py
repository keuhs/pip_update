#/usr/bin/env python
# -*- coding: utf-8 -*-

from pip._internal.utils.misc import get_installed_distributions
from subprocess import call

packages = [dist.project_name for dist in get_installed_distributions()]
call("pip install --upgrade " + ' '.join(packages), shell=True)
