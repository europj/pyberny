from setuptools import setup


setup(
    name='berny',
    version='0.1',
    description='Molecular/crystal structure optimizer',
    author='Jan Hermann',
    author_email='dev@hermann.in',
    url='https://github.com/azag0/pyberny',
    packages=['berny'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    license='Mozilla Public License 2.0',
    install_requires=['numpy'],
)
