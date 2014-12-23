from setuptools import setup

setup(
    name='peg_game_sim',
    version='0.0b1',
    description='Solve the CB peg game',
    license='MIT',
    packages=['peggy'],
    entry_points={
        'console_scripts': [
            'peggy=peggy:main',
        ],
    },
)
