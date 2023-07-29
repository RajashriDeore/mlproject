
from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        requirements=[req.replace("/n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Rajashri',
    author_email='rajashrideore2701@gmail.com',
    packages=find_packages(),
    # we can not hard code every package as we may require 100's do we
    # will create function which will take all package names from 'Requirements.txt'
    ## install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('Requirements.txt')
)