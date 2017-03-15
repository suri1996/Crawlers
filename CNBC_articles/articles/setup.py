# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'articles',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = articles.settings']},
    package_data = {
        'articles': ['res/*.csv']
    },
    zip_safe = False,
    include_package_data = True,
)
