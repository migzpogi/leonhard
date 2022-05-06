import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="leonhard",
    version="1.6.5",
    author="Migz Estrella",
    author_email="me@migzestrella.com",
    description="A commons library for Project Euler problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/migzpogi/leonhard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)