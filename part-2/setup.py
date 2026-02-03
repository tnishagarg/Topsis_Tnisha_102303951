from setuptools import setup, find_packages

setup(
    name="Topsis-Tnisha-102303951",
    version="1.0.5",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        'console_scripts': [
            'topsis=Topsis_Tnisha_102303951.topsis:main',
        ],
    },
    author="Tnisha",
    description="A Python package for TOPSIS decision making",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
