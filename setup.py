from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_attribute(file_path:str)->List[str]:
    '''This function returns the list of required packages'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author="Sanyam",
    author_email="sanyam.verma@gmail.com",
    packages=find_packages(),
    requires=get_attribute('requirements.txt')

)