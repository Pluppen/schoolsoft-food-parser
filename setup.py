import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="schoolsoft_food_parser",
    version="0.0.2",
    author="Elias Juremalm",
    author_email="eliass.juremalm@gmail.com",
    description="A package for parsing food sheet from schoolsoft",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pluppen/schoolsoft-food-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
