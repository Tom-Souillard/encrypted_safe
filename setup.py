from setuptools import setup, find_packages

setup(
    name='encrypted_safe',
    version='0.1.0',
    author='Tom Souillard',
    author_email='tom.souillard@gmail.com',
    description='A secure file encryption tool for individuals and businesses',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Tom-Souillard/encrypted_safe',
    packages=find_packages(),
    install_requires=[
        'PyQt5>=5.15.6',
        'cryptography>=38.0.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Security',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'encrypted_safe=encrypted_safe.main:main',
        ],
    },
)
