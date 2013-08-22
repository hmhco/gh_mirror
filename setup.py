# -*- coding: utf-8; -*-
#   Copyright [2013] [Robert Allen]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import os
from setuptools import setup
from gh_mirror import __version__

setup(
    name='gh_mirror',
    version=__version__,
    description='A tool to mirror and maintain github repositories.',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'readme.rst'
        )
    ).read(),
    install_requires=[
        'requests'
    ],
    author='Robert Allen',
    author_email='zircote@gmail.com',
    license='Apache-2.0',
    url='http://github.com/zircote/gh_mirror',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: System :: Networking :: Monitoring'
    ],
    entry_points={
        'console_scripts': [
            'gh_mirror = gh_mirror.cli:main',
        ],
    },
    zip_safe=False,
    packages=['gh_mirror'],
    include_package_data=True,
)
