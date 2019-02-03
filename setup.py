import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as rf:
    install_requires = rf.read().splitlines()

setuptools.setup(
    name='wordpy',
    version='1.0.2',
    url='https://github.com/mentix02/wordpy',
    license='MIT',
    author='manan',
    author_email='manan.yadav02@gmail.com',
    description='A dictionary program for nix* terminals',
    packages=['wordpy'],
    scripts=['bin/wordpy'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='wordpy dictionary api termdict',
    install_requires=install_requires,
    classifiers=[
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities'
    ]
)
