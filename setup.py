"""Python setup.py for code_exercises package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("code_exercises", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="code_exercises",
    version=read("src/code_exercises", "VERSION"),
    description="Awesome code_exercises created by TheeoCornnaro",
    url="https://github.com/TheeoCornnaro/code_exercises/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="TheeoCornnaro",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["code_exercises = code_exercises.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
