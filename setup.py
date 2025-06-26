from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    HYPEN_E_DOT = '-e .'
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip whitespace and newlines
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if present
    return requirements

setup(
    name='datascience',
    version='0.0.1',
    author='Ratnam',
    author_email='ratnamojha71@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
) 
