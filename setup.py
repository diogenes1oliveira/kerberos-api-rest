# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

__version__ = "0.1.0"
__doc__ = "A REST API for Kerberos' kadmin"

import io
import re

from setuptools import find_packages, setup


def get_requirements_file(fp):
    reqs = []
    for line in fp:
        line = line.strip()
        if not line or re.match(r'\s*#', line):
            continue
        reqs.append(line)
    return reqs


with io.open('requirements.txt', encoding='utf8') as fp:
    run_requirements = get_requirements_file(fp)
with io.open('requirements.dev.txt', encoding='utf8') as fp:
    dev_requirements = get_requirements_file(fp)
with io.open('README.md', encoding='utf8') as fp:
    long_description = fp.read()

setup(
    name="kerberos-rest-api",
    version=__version__,
    author="Diógenes Oliveira",
    author_email="diogenes1oliveira@gmail.com",
    packages=['kerberos_rest_api'],
    include_package_data=True,
    url="https://github.com/diogenes1oliveira/kerberos-rest-api",
    license="MIT",
    description=__doc__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
        'dev': dev_requirements,
    },
    data_files=[],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=("kerberos", "rest"),
    entry_points={
        'console_scripts': [
            'kerberos-rest-api = kerberos_rest_api.__main__:main',
        ],
    },
)
