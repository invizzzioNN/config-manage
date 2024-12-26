from setuptools import setup, find_packages

setup(
    name="config_parser",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["toml"],
    entry_points={
        "console_scripts": [
            "config-parser=main:main",
        ],
    },
)