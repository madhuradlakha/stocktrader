from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='StockTrader',
      version=version,
      description="It helps one know the value of their stock",
      long_description="""\
This application lets you know the value of your stock in an instant, without having to surf the net and going through links with umpteen ads. It also shows you current situation of the market! It also gives updates as to how much it has increased/decreased in that day. More updates coming soon, will give more features.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='stock stocktrader bse nse market bear bearish bull bullish profit loss share shares stocks price value',
      author='Madhur Adlakha',
      author_email='madhuradlakha@yahoo.co.in',
      url='www.madhuradlakha.com',
      license='NA',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
