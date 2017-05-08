from setuptools import setup

setup(
    name="ppt-time-referee",
    version='0.1',
    py_modules=['referee'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ppt-ref=referee:cli
    ''',
)
