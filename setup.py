import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding = 'utf-8') as f:
	long_description = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), encoding='utf-8') as f:
	requirements_list = [line.rstrip('\n') for line in f]

setup(
	name = 'FreqObjectOps',
	packages = ['FreqObjectOps'],
	version = '0.0',
	license = 'MIT',
	description = 'Some special functions for some python objects.',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	author = 'Samyak Ratna Tamrakar',
	author_email = 'samyak.r.tamrakar@gmail.com',
	url = 'https://github.com/srtamrakar/python-general-functions',
	# download_url = 'https://github.com/srtamrakar/python-general-functions/archive/v_0.0.tar.gz',
	keywords = ['list', 'string', 'datetime', 'directory'],
	install_requires = requirements_list,
	classifiers = [
		'Development Status :: 1 - Planning',  # Either"3 - Alpha", "4 - Beta" or "5 - Production/Stable"
		'Intended Audience :: Developers',  # Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7'
	],
)
