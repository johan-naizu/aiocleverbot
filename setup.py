from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf8') as f:
	long_description = f.read()

with open('requirements.txt') as f:
	requirements = f.read().splitlines()

setup(
	name='aiocleverbot',
	version='1.0.0',
	author='Johan Naizu',
	author_email='johan@naizu.in',
	description='Async library for cleverbot',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/johan-naizu/aiocleverbot',
	packages=find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
            ],
	install_requires=requirements
)
