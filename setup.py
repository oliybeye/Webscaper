from setuptools import setup

setup(
    name='CraiglistScraper',
    version='0.1',
    description='Craiglist web scraper',
    author='Oliyad Beyene',
    url='https://github.com/oliybeye/Webscaper',
    packages=['dist/', 'distutils.command'],
    install_requires=[
        'requests',
        'beautifulsoup4',
        'setuptools',
    ]
)
