import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gt3x-muschellij2", # Replace with your own username
    version="0.0.2",
    author="Shaheen Syed",
    author_email="shaheen.syed@uit.no",
    description="A package to read extract raw acceleration data from .gt3x files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaheen-syed/gt3x",
    packages=setuptools.find_packages(exclude = "tests"),  # Required
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",    
    python_requires='>=3.6',
)