import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-worldwide",
    version = "0.1",
    url = 'http://github.com/un33k/django-worldwide',
    license = 'BSD',
    description = "An app to manage all cities, states, countires in the world",
    long_description = read('README'),
    author = 'Val L33',
    author_email = 'val@neekware.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 1 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)