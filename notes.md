notes taken following this [YouTube tutorial](https://www.youtube.com/watch?v=GIF3LaRqgXo&t=3s)

choose a unique name for your package: here we are going to use _publishtutorial_, so if you want to repeat the passages, choose a new name, not present on PyPI

First version of setup.py (not really the one of the video but useful to start)

```python
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()
setup(
    name='publishtutorial',
    version='0.0.1',
    description='Hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["myfunc"],
    package_dir={'':'src'},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
```

after building package with
```bash
python3 setup.py bdist_wheel
```

do
```bash
pip3 install -e .
```
this links to the code we want to install instead of copying it twice

now if we open a python terminal from the base directory, we can already import the functions of the package
```python
>>> from myfunc import say_hello()
>>> say_hello()
'Hello world'!
```

After adding some requirements to the setup.py file in this way (for the moment no requirements.txt file):
```python
setup(
    ...,
    install_requires=[
        'pandas==2.0.3',
        'meteostat'
    ],
    ...
)
```

re-run from terminal without building again:
```
pip install -e .
```

To install package, along with the tools you need to develop and run tests, add the following argument in the setup.py file
```python
setup(
    ...,
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ]
    },
    ...
)
```
and run the following in your virtualenv:
```bash
$ pip3 install -e .[dev]
```

add a test file like test_publishtutorial.py and run (note that it is in the base folder and it is capable of calling myfunc in the src folder because we specified where to look in the setup.py)
```bash
pytest
```

now we want to also run setup.py with sdist, but before we have to specify a reference repo, an author and an email.
Let's add them to the setup.py (after creating a git repository on github)
```python
setup(
    ...,
    url="https://github.com/matteobollettino/publish_tutorial",
    author="Matteo Bollettino",
    author_email="matteo.bollettino@moxoff.com",
    ...
)
```

and then run
```bash
python setup.py sdist
```

a tar.gz has been created in the dist folder, if you try
```bash
tar tzf dist/publishtutorial-0.0.1.tar.gz
```
to see the files inside, the license and the test_publishtutorial.py are missing.
We need a manifest file:
```bash
# you should add check-manifest to the dev requirements in the setup.py
$ pip3 install check-manifest 

# this gives a sort of warning but it should create the MANIFEST file with the
# include *.something
$ check-manifest --create

$ git add MANIFEST.in
```

now build again with sdist and if you check with tar tzf you see the license and the test_publishtutorial.py file

In the end to build both wheel and tar gz files, simply run:
```bash
python3 setup.py bdist_wheel sdist
```

then to upload (you need to register to PyPI):
```bash
# Put this in the dev requirements too
$ pip3 install twine

$ twine upload dist/*
Insert username and password
```

to update the package after some modifications,
CHANGE VERSION, build the new package and then
```bash
# Check if everything is ok
$ twine check dist/*

# Dist also includes previous versions
$ cd dist
$ twine upload --repository-url https://upload.pypi.org/legacy/ NAME-VERSION-py3-none-any.whl NAME-VERSION.tar.gz
```