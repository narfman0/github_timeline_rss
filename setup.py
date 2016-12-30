#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'flask',
    'requests',
]

test_requirements = [
    'coverage',
    'flake8',
    'tox',
]

setup(
    name='github_timeline_rss',
    version='1.0.0',
    description="Github timeline to RSS translation for easier feed integration",
    long_description=readme,
    author="Jon Robison",
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/github_timeline_rss',
    packages=[
        'github_timeline_rss',
    ],
    package_dir={'github_timeline_rss':
                 'github_timeline_rss'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='github_timeline_rss',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
