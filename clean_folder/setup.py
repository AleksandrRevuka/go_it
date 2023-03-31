"""Setup"""
from setuptools import setup, find_namespace_packages

setup(
    name='clean folder',
    version='0.0.1',
    description='Script, which sort the folder',
    author='Alex',
    author_email='Asmo@hotmail.com',
    url='https://github.com/AleksandrRevuka/go_it.git',
    license='MIT',
    classifiers=[
        "Programming Language :: Paython :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    data_files=[
        ('clean_folder', ['clean_folder/README.md', 'clean_folder/LICENSE'])],
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder=clean_folder.sort:main']}
)
