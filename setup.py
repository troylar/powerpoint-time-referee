from distutils.core import setup

setup(
    name="ppt-time-referee",
    version='0.7.3',
    packages=['time_referee'],
    py_modules=['referee'],
    description='Simple time-awareness tool for PowerPoint presentations',
    author="Troy Larson",
    author_email='troylar@gmail.com',
    install_requires=[
        'Click','arrow','python-pptx'
    ],
    entry_points='''
        [console_scripts]
        ppt-ref=referee:cli
    ''',
)
