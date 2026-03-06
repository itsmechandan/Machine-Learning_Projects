from setuptools import find_packages,setup 
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(x:str) -> List[str]:
    '''
    This function would return the list of requirements
    '''
    req = []
    with open(x) as y:
        req = y.readlines()
        req = [i.strip() for i in req if i.strip() and not i.startswith('#')]
        if  HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
        return req 

setup(
name ='baseMl',
version = '0.0.1',
author = 'chandan',
author_email = 'jakkavenkatchandan@gmail.com',
packages = find_packages(),
install_requires= get_requirements('requirements.txt')
)

## Find_packages would basically go to each folder inside the Deployed Projects repository
## and would try to find the __init__.py
