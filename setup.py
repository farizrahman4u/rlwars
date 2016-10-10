from setuptools import setup
from setuptools import find_packages


setup(name='rlwars',
      version='0.0.1',
      description='Framework for deploying reinforcement learning agents in multiplayer games',
      author='Fariz Rahman',
      author_email='farizrahman4u@gmail.com',
      url='https://github.com/farizrahman4u/rlwars',
      download_url='https://github.com/farizrahman4u/rlwars',
      license='GPL',
      install_requires=['keras'],
      packages=find_packages())
