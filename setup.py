from setuptools import setup
import os
from glob import glob

package_name = 'delivery_robot_pkg'

object_detection_module ="delivery_robot_pkg/ObjectDetection"

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, object_detection_module],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('lib', package_name), glob('scripts/*')),
        (os.path.join('share', package_name,'worlds'), glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ansoatc',
    maintainer_email='anselmeatchogou@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawner_node = delivery_robot_pkg.sdf_spawner:main',
            'video_recording_node = delivery_robot_pkg.video_save:main',
        ],
    },
)
