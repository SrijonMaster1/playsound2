from inspect import getsource
from os.path import abspath, dirname, join
from setuptools import setup

here = abspath(dirname(getsource(lambda: 0)))

with open('README.md', encoding='utf-8') as long_description_file:
    long_description = long_description_file.read()

setup(name='playsound2',
    version='0.1',
    description=long_description,
    long_description=long_description,
    url='https://github.com/kethan1/playsound2',
    author='Kethan Vegunta',
    author_email='kethan@vegunta.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Sound/Audio :: MIDI',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3'
    ],
    keywords='sound playsound music wave wav mp3 media song play audio',
    py_modules=['playsound']
)
