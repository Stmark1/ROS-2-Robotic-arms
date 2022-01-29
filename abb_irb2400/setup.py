import os
from glob import glob
from setuptools import setup

package_name = 'abb_irb2400'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),

        (os.path.join('share', package_name, 'meshes/irb2400/collision'), glob('meshes/irb2400/collision/*')),
        (os.path.join('share', package_name, 'meshes/irb2400/visual'), glob('meshes/irb2400/visual/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stmark',
    maintainer_email='stmark.1.mr@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
