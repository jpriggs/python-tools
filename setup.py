import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='pythontools',
    version='0.0.1',
    author='Jason Rigdon',
    author_email='jprigdon@gmail.com',
    description='Reusable python tools for development',
    long_description=long_description,
    url='https://github.com/jpriggs/pythontools',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
