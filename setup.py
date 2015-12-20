import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

long_desc = '''torc-web is the web interface for torc, a tool which allows users to specify targets and run sets of tools against them. This tool is designed to make a pentester's life easier and more consistent by allowing them to specify tools they would like to run against targets, without having to type them in a shell or write a script. This tool will probably be useful during certain exams as well..'''

setup(
    name='torc-web',
    version='0.1.0',
    description='Web interface for torc.',
    long_description=long_desc,
    author='Aidan Marlin',
    author_email='aidan.marlin@gmail.com',
    url='https://github.com/rascal999/torc-web',
    license='GNU Affero GPL v3',
    packages=['torc_application'],
    install_requires=[
        'PyYAML', 'screenutils', 'inquirer',
        'readchar<=0.7' # https://github.com/magmax/python-inquirer/issues/8
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': ['torc-web = torc_application:create_app']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'Environment :: Console'],
    keywords='torc-web pentest automate toolset hack'
)
