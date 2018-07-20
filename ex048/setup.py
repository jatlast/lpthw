try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LPTHW Ex48'
    , 'author': 'Jason Baumbach'
    , 'url': 'http://???'
    , 'download_url': 'http://???'
    , 'author_email': 'jatlast@hotmail.com'
    , 'version': '0.1'
    , 'install_requires': ['nose']
    , 'packages': ['ex048']
    , 'scripts': []
    , 'name': 'ex048'
}

setup(**config)
