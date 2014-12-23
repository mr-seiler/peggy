from setuptools import setup

setup(
    name='peg_game_sim',
    version='0.0b1',
    description='Solve the CB peg game',
    url='https://github.com/mr-seiler/peggy',
    license='MIT',
    packages=['peggy'],
    extras_require={
        'dev': ['pytest','coverage'],
    },
    entry_points={
        'console_scripts': [
            'peggy=peggy:main',
        ],
    },
)
