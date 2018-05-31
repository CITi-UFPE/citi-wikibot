from setuptools import setup

with open('README.rst', 'r') as f:
  readme = f.read()

with open('requirements.txt', 'r') as file:
    requires = [line.strip('\n') for line in file]

setup(
  name='citi-wikibot',
  packages=['wikibot'],
  version='0.4.10',
  description='CITI\'s Wiki page editing for lazy people.',
  long_description=readme,
  author='Vanessa Barreiros',
  author_email='vanessa.barreiros@citi.org.br',
  url='https://github.com/citi-ufpe/citi-wikibot',
  keywords=['wiki', 'bot', 'wikibot', 'citi'],
  install_requires=requires
)