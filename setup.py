import os
from setuptools import setup, find_packages

module_version = "0.1.5"

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

dependencies_list = [
    "pandas>=1.1.3",
    "pytest>=6.1.2",
    "Unidecode>=1.1.1",
]

setup(
    name="FreqObjectOps",
    packages=find_packages(),
    version=module_version,
    license="MIT",
    description="Some special functions for some python objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Samyak Ratna Tamrakar",
    url="https://github.com/srtamrakar/python-general-functions",
    download_url=f"https://github.com/srtamrakar/python-general-functions/archive/v_{module_version}.tar.gz",
    keywords=["list", "string", "datetime", "directory", "path"],
    install_requires=dependencies_list,
    classifiers=[
        "Development Status :: 4 - Alpha",  # Either"3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Database :: Database Engines/Servers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
