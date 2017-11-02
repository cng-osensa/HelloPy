from distutils.core import setup

setup(
  name = 'testpackage',
  packages = ['testpackage'], # this must be the same as the name above
  version = '0.1',
  description = 'A random test lib',
  author = 'Caleb Ng',
  author_email = 'cng@osensa.com',
  url = 'https://github.com/cng-osensa/HelloPy/', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)