from setuptools import find_packages, setup

package_name = 'my_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sumayya',
    maintainer_email='sumayamazhar006@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_node = my_turtle_package.my_node:main',
            'move_turtle = my_turtle_package.move_turtle:main',
            'move_circle = my_turtle_package.move_circle:main',
            'move_triangle = my_turtle_package.move_triangle:main',
            'move_multi = my_turtle_package.move_multi:main',
        ],
    },
)
