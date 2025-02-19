from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "quickmlops"
LONG_DESCRIPTION = "MLOPs SDK"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="quickmlops",
    version=VERSION,
    author="Jordo993",
    author_email="jordan.m.young0@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["toml"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python3", "mlops", "machine learning"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
)
