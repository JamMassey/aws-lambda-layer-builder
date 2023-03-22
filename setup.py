import setuptools

setuptools.setup(
    name='pylayerize',
    keywords='aws lambda layer pylayerize pylayerizer pylayerize',
    description='pylayerize simplifies the process of creating AWS Lambda Layers by leveraging Docker to compile and package Python dependencies for any targeted runtime. With support for custom packages and private GitHub repos, pylayerize optimizes the creation and deployment of Lambda Layers for improved development efficiency.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    package_data={
        'pylayerize': ['dockerfiles/*']
    },
    include_package_data=True,
    install_requires=[],
    packages=setuptools.find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'pylayerize=pylayerize.__main__:main',
        ],
    },
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
	python_requires='>=3.7',
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    author='James Massey',
    author_email='jammassey@hotmail.com',
    url='https://github.com/JamMassey/lambda-layer-builder',
)