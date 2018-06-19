import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="License2Deploy",
    version="0.2.0",
    author="Dun and Bradstreet",
    author_email="license2deploy@dandb.com",
    description="Rolling deploys by changing desired amount of instances AWS EC2 Autoscale Group",
    license="GPLv3",
    keywords="AWS EC2 AutoScale Group AMI desired capacity",
    url="https://github.com/dandb/License2Deploy",
    packages=['License2Deploy'],
    entry_points={
        'console_scripts': [
            'rolling_deploy = License2Deploy.rolling_deploy:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        'boto==2.48.0',
        'boto3==1.7.37',
        'PyYAML==3.12',
        'retry==0.9.2'
    ],
    extras_require={'test': [
        'coverage',
        'mock',
        'moto',
        'placebo',
        'pytest',
    ]},
    long_description=read('README.md'),
)
