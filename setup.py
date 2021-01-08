# coding: utf-8
#
# This code is part of lattpy.
#
# Copyright (c) 2021, Dylan Jones
#
# This code is licensed under the MIT License. The copyright notice in the
# LICENSE file in the root directory and this permission notice shall
# be included in all copies or substantial portions of the Software.

from setuptools import setup, find_packages
import versioneer


def requirements():
    with open("requirements.txt", "r") as f:
        return f.readlines()


def long_description():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name='lattpy',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Dylan Jones',
    author_email='dylanljones94@gmail.com',
    description='Python package for modeling bravais lattices',
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/dylanljones/lattpy',
    packages=find_packages(),
    license='MIT License',
    install_requires=requirements(),
    python_requires='>=3.6',
)
