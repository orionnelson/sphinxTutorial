## Sphinx Install Directions
### Setup 
1. Create a venv 
```bash
python or python3 -m venv . sphinx-tutorial
```
2. Activate Virtual Python Environment
```bash
# On Linux
source sphinx-tutorial/bin/activate
# On Windows
cd sphinx-tutorial/Scripts && activate
```

3. Install Extensions for Scripting
```bash
# If pip is not on path try python -m pip
pip install -r requirements.txt 
# use pipreqs package
python -m pipreqs . # dir with *.py
# instead of
pip freeze >> requirements.txt 

# For toml based packages 
pip install -e . # base pkg
pip install -e .[doc] # optional dep
```
- Install vscode extensions for parsing sphinx
3. Quickstart Sphinx
```bash
#Quickstart Docs
sphinx-quickstart docs
# root path docs
# sep source / build: y
# language: en
```
4. Test Make Docs
```bash
cd docs && make html
# Run docs with built in python server
>new terminal
 cd docs/build/html && python -m http.server 
 ```
 4. Transfer Restructured Text to Markdown with Myst-parser
 ```bash
 pip install rst-to-myst[sphinx]
 rst2myst convert docs/**/*.rst
 #delete index.rst
 add 
 extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.autosectionlabel",
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
] 
 to docs/source/conf.py
 add 
 import sys
 import os
 sys.path.insert(0, os.path.abspath('../../Examples'))

 and add 'furo' to html_theme
```
5. Sphinx Autobuild Automation
```bash
pip install sphinx-autobuild
# Run auto build in background if you like
sphinx-autobuild docs/source docs/build/html
```

6. Simplify Build File
```bash
remove *
docs/build/index.md
*```
{include}../../README.md
:relative-images:
*```
*```{warning}
This is a random warning 
*```
```

7. Add the following to docs/build/index.md
Under toctree
```bash
examples

#in examples.md add the following
remove *
## async
*```{eval-rst}
.. automodule:: async_example
   :members:
*```
## class
*```{eval-rst}
.. automodule:: class_person_example
   :members:
*```
## function
*```{eval-rst}
.. automodule:: function_example
   :members:
*```
## inheritance
*```{eval-rst}
.. automodule:: inheritance_petstore
   :members:
*```
```






 