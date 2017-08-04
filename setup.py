from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'Adafruit_Video_Looper',
      version           = '1.0.0',
      author            = 'Jon Snow',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Application to turn your Raspberry Pi into a dedicated looping video playback device, good for art installations, information displays, or just playing cat videos all day.',
      license           = 'GNU GPLv2',
      url               = 'https://github.com/xmr-smithx/NewProyect',
      install_requires  = ['pyudev'],
      packages          = find_packages())
