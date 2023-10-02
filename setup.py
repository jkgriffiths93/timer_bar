from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="timer_bar",
    version="0.0.9",
    author="Jeff Griffiths",
    author_email="jkgriffiths93@gmail.com",
    description="Simple graphic to show progress of a process",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Homepage": "https://github.com/jkgriffiths93/timer_bar",
    },
    install_requires=[
    ],
)
