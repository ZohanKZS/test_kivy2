[app]

# (str) Title of your application
title = My App ZZZ

# (str) Package name
package.name = myappzzz

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ZohanKZS

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py,png,jpg,kv,atlas,po,mo

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.0.0

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/logo/presplash512okmin.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/logo/logo512min.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = all

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY