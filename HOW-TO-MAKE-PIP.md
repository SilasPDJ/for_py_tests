# Make sure you have upgraded version of pip

Windows

```
py -m pip install --upgrade pip
```

Linux/MAC OS

```
python3 -m pip install --upgrade pip
```

## Create a project with the following structure

```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
touch LICENSE
touch pyproject.toml
touch setup.cfg
mkdir src/mypackage
touch src/mypackage/__init__.py
touch src/mypackage/main.py
mkdir tests
```

## pyproject.toml

# Setup.cfg setup

```
# Running the build
### Make sure your build tool is up to date
```

py -m pip install --upgrade build

```


### Create the build
```

py -m build

```
### twine part
#### for tests

```

pip install twine
py -m twine upload --repository testpypi dist/\*

```

### para ir para o repositório Test.pypi...

twine upload dist/\*

### para ir para o PYPI

```

### References

https://packaging.python.org/tutorials/packaging-projects/
https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
https://www.youtube.com/watch?v=v4bkJef4W94&ab_channel=DevOpsJourney

```

```
