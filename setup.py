from setuptools import setup, find_packages

setup(
    name="tldrr",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "openai"
    ],
    entry_points={
        'console_scripts': [
            'tldrr=tldrr.tldrr:main',
        ],
    },
    author="Danny",
    author_email="emtoor@gmail.com",
    description="A CLI tool that extends TLDR output with GPT-generated examples",
    keywords="tldr, cli, openai, gpt, python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)