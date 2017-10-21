from setuptools import setup, find_packages
from codecs import open
import os

from metrics import __version__
here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', format='md', to='rst')
except(IOError, ImportError):
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

# get the dependencies and installs
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and
                    (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='metrics',
    version=__version__,
    description='metrics produces metrics for C, C++, Javascript, and Python programs',
    long_description=long_description,
    license='MIT',
    url='https://github.com/finklabs/metrics/',
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Mark Fink',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='mark@finklabs.de',
    entry_points={
        'console_scripts': [
            'metrics = metrics.metrics:main'
        ]
    }
)
