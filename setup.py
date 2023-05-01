from setuptools import find_packages, setup
from io import open

readme = open('README.md', encoding='utf-8').read()

setup(
    name='django-mcq',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A configurable quiz app for Django.',
    long_description=readme,
    url='https://github.com/suhailvs/django-mcq',
    author='Suhail VS',
    author_email='suhailvs@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=4.0.0'
    ]
)