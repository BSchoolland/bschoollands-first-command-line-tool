from setuptools import setup, find_packages

setup(
    name="bschoollands_first_package", 
    version="0.1.1",
    author="Benjamin Schoolland",
    author_email="bschoolland@gmail.com",
    description="Ben Schoolland's first ever Python package!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BSchoolland/bschoollands-first-command-line-tool",
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bschoollands_first_package=bschoollands_first_package.bschoollands_first_package:main',  # Format: 'command=module:function'
        ],
    },
    python_requires=">=3.6", # not sure if this is necessary but it's in the example
    install_requires=[
        # Add your dependencies here (if any)
    ],
)
