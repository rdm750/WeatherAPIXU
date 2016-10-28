from distutils.core import setup

version = '0.0.2'

PACKAGES = ['WeatherAPIXU']

setup(
    name='WeatherAPIXU',
    version= version,
    author ='Rohit Malgaonkar http://github.com/rdm750',
    author_email ='rdm750@gmail.com',
    description='Get Weather using API Apixu.com',
    packages= PACKAGES,
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Software Development :: Libraries :: Application Frameworks',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Intended Audience :: Developers' ],
)
