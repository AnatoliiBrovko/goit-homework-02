from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.2',
    description='Homework code',
    url='https://github.com/AnatoliiBrovko/goit-homework-02',
    author='Anatolii Brovko',
    author_email='ing@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)