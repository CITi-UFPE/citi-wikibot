from setuptools import setup

with open('README.rst', 'r') as f:
  readme = f.read()

setup(
  name='citi-wikibot',
  packages=['wikibot'],
  version='0.4.14',
  description='CITi Wiki pages editing with Python made easy.',
  long_description=readme,
  author='Vanessa Barreiros',
  author_email='vanessa.barreiros@citi.org.br',
  url='https://github.com/citi-ufpe/citi-wikibot',
  keywords=['wiki', 'bot', 'wikibot', 'citi'],
  install_requires=[
    'requests',
    'tapioca-github',
    'misaka',
    'python-decouple'
  ],
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Development Status :: 2 - Pre-Alpha',
    'Topic :: Utilities'
  ]
)
