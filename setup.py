from setuptools import setup, find_packages
setup(
    name="ConvertPath",
    version="0.1",
    packages=find_packages(),

    install_requires=['pathlib'],

    # metadata to display on PyPI
    author="Shinya Akagi",
    author_email="dummy@example",
    description="Simple Path Converter for converting windows path (C:\hoge) to linux path (/C/hoge)",
    license="PSF"
)
