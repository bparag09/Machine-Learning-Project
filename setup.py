from typing import List
from setuptools import setup, find_packages



#Declaring variable for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Parag Bhardwaj"
DESCRIPTION="This the first FSDS Nov batch ML Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME = 'requirements.txt'


def get_requirements_list()->List[str]:
    """
    Description: This function returns list of requirementts mentioned in requirements.txt file

    Returns a list which contain names of libraries.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')


setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires=get_requirements_list()
    )