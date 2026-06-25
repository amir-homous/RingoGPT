from setuptools import setup, find_packages

setup(
    name="ringogpt",
    version="0.1.0",
    description="A lightweight CLI assistant that converts natural language into safe Linux shell commands.",
    author="Amir Hossein Mousavi",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "soal=ringogpt.cli:main",
            "ringogpt=ringogpt.cli:main",
        ]
    },
)
