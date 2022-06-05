from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="algoaid",
    version="1.0.2",
    description="Tools for learning about algorithms and data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emilostuff/algoaid",
    author="Emil Skydsgaard",
    author_email="emilostuff@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="student, learning, algorithms, data, structures",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8, <4",
    install_requires=["matplotlib", "graphviz", "scipy", "numpy"],
)
