try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'PROJECT NAME',
    'author': 'Cameron',
    'url': 'URL',
    'download_url': 'DOWNLOAD SOURCE',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)

