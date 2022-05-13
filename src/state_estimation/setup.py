from setuptools import setup
import os
from glob import glob

package_name = 'state_estimation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='basti',
    maintainer_email='sebastian.mai@ovgu.de',
    description='package for state estimation',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'scoring = state_estimation.scoring:main',
            'filter = state_estimation.filter:main',
            'locator = state_estimation.locator:main',
        ],
    },
)
