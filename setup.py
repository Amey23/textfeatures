from setuptools import setup

def readme():
    with open('README.md', encoding="utf8") as f:
        README = f.read()
    return README
	

setup(
    name="textfeatures",
    version="0.0.1",
    description="A Python package to get basic features from the text data.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Amey23/textfeatures",
    author="Amey Band",
    author_email="ameypband23@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["textfeatures"],
    include_package_data=True,
    install_requires=["nltk"],
    )