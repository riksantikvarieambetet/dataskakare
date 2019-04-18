from setuptools import setup
version = '0.2.0'
repo = 'dataskakare'

setup(
  name = 'dataskakare',
  packages = ['dataskakare'],
  install_requires=['requests', 'google-auth', 'google-cloud-vision', 'google-cloud-translate'],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  python_requires='>=3.6.0',
  version = version,
  description = 'Python package with not so common data wrangling functions and API wrappers.',
  author = 'Albin Larsson',
  author_email = 'albin.larsson@raa.se',
  url = 'https://github.com/riksantikvareambetet/' + repo,
  download_url = 'https://github.com/riksantikvareambetet/' + repo + '/tarball/' + version,
  keywords = ['heritage', 'cultural'],
  license='MIT',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3 :: Only',
    'Intended Audience :: Developers',
    'Intended Audience :: Education'
  ]
)
