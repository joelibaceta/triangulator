import sys
from setuptools import setup, find_packages

setup(
    name="triangulator",
    version="1.0.2",
    author="Joel Ibaceta",
    author_email="mail@joelibaceta.com",
    license='MIT',
    description="A simple tool to calc triangles for any polygon",
    long_description="A simple tool to calc triangles for any polygon",
    url="https://github.com/joelibaceta/triangulator",
    project_urls={
        'Source': 'https://github.com/joelibaceta/triangulator',
        'Tracker': 'https://github.com/joelibaceta/triangulator/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='triangles, polygon, triangulator',
)