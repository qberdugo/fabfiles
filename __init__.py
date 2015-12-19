# coding: utf-8

import glob
import os

from fabric.api import env

user_fabfiles_dir = os.path.split(__file__)[0]

fabfiles = glob.glob(os.path.join(user_fabfiles_dir, '*.fab'))
fabfiles += glob.glob(os.path.join(user_fabfiles_dir, '*.fab.local'))
fabfiles.sort()

project_fabfile_path = os.path.join(os.getcwd(), 'fabfile.py')
if os.path.exists(project_fabfile_path):
   env.real_fabfile = project_fabfile_path
   fabfiles += [project_fabfile_path]

# Load user and project (if any) fabfiles
for fabfile in fabfiles:
    execfile(fabfile)

