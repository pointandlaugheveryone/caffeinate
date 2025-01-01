import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pykupi",
    version="0.0.1",
    author="Mikhail Smolnikov",
    author_email="smolnik.mikhail@gmail.com",
    description="The easiest way to getting prices from kupi.cz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prostmich/pykupi",
    project_urls={"Bug Tracker": "https://github.com/prostmich/pykupi/issues"},
    license="MIT",
    packages=find_packages(),
    install_requires=["aiohttp>=3.7.2,<4.0.0", "bs4==0.0.1", "pydantic>=1.9.0"],
)
