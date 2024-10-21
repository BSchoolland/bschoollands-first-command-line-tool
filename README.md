# BSchoolland's first package
This repository is for my first ever PyPi package. It's a simple, useless package designed to help me learn how to create and publish packages to PyPi.

# Test PyPi link:
https://test.pypi.org/project/bschoollands-first-package/0.1.2/
# How I built and published this package
First, I used wheel to build the package 
```bash
 pip install setuptools wheel
 python setup.py sdist bdist_wheel
```
Next I used twine to upload the package to test.pypi.org after creating an account and an api token
```bash
pip install twine
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
After doing this, the package was avalible on the test version of pypi!
