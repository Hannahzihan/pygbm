from setuptools import setup, find_packages

setup(
    name="pygbm",
    version="0.1",
    description="A Python package for simulating Geometric Brownian Motion",
    author="Hannah",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    entry_points={
        'console_scripts': [
            'pygbm=pygbm.cli:main',
        ],
    },
)
