from setuptools import setup, find_packages
setup(
    name="ConvertPath",
    version="0.1",
    packages=find_packages(),

    install_requires=['pathlib'],

    # metadata to display on PyPI
    author="Shinya Akagi",
    author_email="dummy@example",
    description="Simple Path Convertor",
    long_description="Simple Path Convertor for converting windows path ('C:\hoge') to linux path ('/C/hoge')",
    url="https://github.com/ShinyaAkagiI/convertpath", 
    license="PSF",
)
