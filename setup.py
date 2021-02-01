import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name="vans-eightball",
    version="0.0.1",
    description="Provides wise answers to tough problems",
    long_description=README,
    long_description_content_type="text/markdown",
    # url="https://github.com/realpython/reader",
    author="Van Ly",
    author_email="vancly@hotmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "eightball=src.van.eightball:get_answer",
        ]
    },
)