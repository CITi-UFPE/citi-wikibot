from distutils.core import setup

with open('README.md') as f:
  readme = f.read()

with open('LICENSE.txt') as f:
  license = f.read()

setup(
  name='citi-wikibot',
  packages=['wikibot'],
  version='0.4.2',
  description='CITI\'s Wiki page editing for lazy people.',
  long_description=readme,
  long_description_content_type='text/markdown',
  author='Vanessa Barreiros',
  author_email='vanessa.barreiros@citi.org.br',
  url='https://github.com/citi-ufpe/citi-wikibot',
  keywords=['wiki', 'bot', 'wikibot', 'citi'],
  license=license,
  install_requires=[
    'requests',
    'misaka'
  ]
)