# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Date: 2020/10/14 13:58
Desc: MSSDK 的 PYPI 基本信息文件
"""
import re
import ast

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_version_string():
    """
    get the mssdk version number
    :return: str version number
    """
    with open("mssdk/__init__.py", "rb") as file:
        version_line = re.search(
            r"__version__\s+=\s+(.*)", file.read().decode("utf-8")
        ).group(1)
        return str(ast.literal_eval(version_line))


setuptools.setup(
    name="mssdk",
    version=get_version_string(),
    author="maxsmart",
    author_email="298038875@qq.com",
    license="MIT",
    description="Python SDK for MaxSmart!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cdmaxsmart/mssdk",
    packages=setuptools.find_packages(),
    install_requires=[
        "bs4>=0.0.1",
        "lxml>=4.2.1",
        "matplotlib>=3.1.1",
        "numpy>=1.15.4",
        "pandas>=0.25",
        "requests>=2.22.0",
        "demjson>=2.2.4",
        "pyexecjs>=1.5.1",
        "pillow>=6.2.0",
        "pypinyin>=0.35.0",
        "websocket-client>=0.56.0",
        "html5lib>=1.0.1",
        "scikit-learn>=0.22",
        "fonttools>=4.2.2",
        "xlrd>=1.2.0",
        "tqdm>=4.43.0",
        "openpyxl>=3.0.3",
        "jsonpath>=0.82",
        "tabulate>=0.8.6",
        "decorator>=4.4.2",
        "mplfinance>=0.12.3a3",
    ],
    package_data={"": ["*.py", "*.json", "*.pk", "*.woff", "*.js"]},
    keywords=["finance"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
