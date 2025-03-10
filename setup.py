from setuptools import setup, find_packages

setup(
    name="nsopen",
    version="0.1.0",
    arthur="Nelson Chan",
    description="a tool to perform DNS lookup and open IP addresses in a browser",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/khchanel/nsopen",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={ 
        # pip install -e .[dev]
        'dev': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'nsopen=nsopen.cli:main',
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
