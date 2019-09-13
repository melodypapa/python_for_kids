from setuptools import setup, find_packages

setup(
    name='python_for_kids',
    version = '0.0.1',
    license = 'proprietary',
    description="Teach the python language for the kids",

    author = 'melodypapa',
    author_email = "melodypapa@outlook.com",
    url="",

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    #install_requires=['xmltodict'],

    #include_package_data=True,
    
    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'python_kids        = python_kids.cli.python_kids:main',
        ]
    }
)