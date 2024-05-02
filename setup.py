import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='joshnator',
    version='0.0.4',
    author='Joshua Nishanth',
    author_email='joshuanishanth120@gmail.com',
    description='Data cleaning package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Joshuaakaspace/joshnator', 
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.5',
    install_requires=[
        'pandas>=1.0',
        'numpy>=1.15',
    ]
)

