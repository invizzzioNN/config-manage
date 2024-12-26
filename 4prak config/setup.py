from setuptools import setup, find_packages

setup(
    name="uvm_project",
    version="1.0.0",
    description="Ассемблер и интерпретатор для учебной виртуальной машины (УВМ)",
    author="Ваше имя",
    packages=find_packages(),
    install_requires=[
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "assembler=main_assembler:main",
            "interpreter=main_interpreter:main"
        ]
    },
)