import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intrepid-ansible", 
    version="0.99.2",
    author="@agrana",
    author_email="alfonso.grana@gmail.com",
    description="An ansible Journey",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agrana/intrepid-ansible",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
