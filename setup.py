from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(

    name= "pacote_idade",
    version= "0.0.1",
    author= "Melissa",
    author_email= "melissajunqueira44@gmail.com",
    description= "Um pacote feito para calcular a idade informada pelo usuário.",
    long_description= page_description,
    long_description_content_type= "text/markdown",
    url= "https://github.com/mikaxhuu/pacote_idade",
    packages= find_packages(),
    install_requires = requirements,
    python_requires = '>= 3.7',

)