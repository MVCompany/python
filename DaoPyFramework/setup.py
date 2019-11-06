import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="daoPyFramework",
    version="0.0.1",
    author="Valentin, Michel",
    author_email="michelvalent@gmail.com",
    description="Dao abstraction helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MVCompany/python/tree/master/DaoPyFramework",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)