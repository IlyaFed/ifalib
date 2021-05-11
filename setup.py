from setuptools import find_packages, setup
import subprocess
from distutils.command.install import install as _install

from distutils.core import setup, Extension

module_rdf = Extension('ifalib.librdf',
                    sources = ['ifalib/rdf.c']) 


# class install(_install):
#     def run(self):
#         subprocess.call(['make', 'clean', '-C', 'ifalib'])
#         subprocess.call(['make', '-C', 'ifalib'])
#         _install.run(self)

setup(
    name='ifalib',
    packages=find_packages(include=['ifalib']),
    # package_data={'ifalib': ['ifalib/librdf.so']},
    # cmdclass={'install': install},
    ext_modules=[module_rdf],
    version='0.1.5',
    description='Ilya Fedorov Analysis',
    author='Ilya Fedorov',
    license='MIT',
    install_requires=[],
    setup_requires=[],
    tests_require=['pytest==4.4.1','pytest'],
)