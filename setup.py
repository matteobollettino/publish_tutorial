from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='publishtutorial', # change this field if you want to create your package
    version='0.0.1',
    description='Hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["myfunc"],
    package_dir={'':'src'},
    install_requires=[
        'pandas==2.0.3',
        'meteostat'
    ],
    extras_require = {
        "dev": [
            "pytest>=3.7",
            "check-manifest>=0.49",
            "twine>=4.0.2",
        ]
    },
    url="https://github.com/matteobollettino/publish_tutorial",
    author="Matteo Bollettino",
    author_email="matteo.bollettino@moxoff.com",
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