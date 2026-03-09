from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='src',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="A Python package that simplifies the creation and execution of unittest test cases.",
    author="Delica Leboe-McGowan",
    author_email="stormindustries22@outlook.com",
    packages=['src'],
    install_requires=[

    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
