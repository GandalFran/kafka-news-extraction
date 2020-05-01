from setuptools import setup

setup(
    name='TIE final project',
    version='1.0',
    description='Final project for the TIE course during 2019-2020 on USAL',
    author='Francisco Pinto Santos and Gabriel Martin Blazquez',
    author_email='franpintosantos@usal.es and gmartinb@usal.es',
    license='see LICENSE.md for details',
    url="http://tiegandalfran.ddns.net",
    packages=['agents', 'utils'],
    install_requires=[
        'flask-request-id-header',
        'confluent-kafka==1.3.0',
        'vaderSentiment==3.2.1',
        'newsapi-python',
        'lxml==4.5.0',
        'cssselect==1.1.0',
        'requests==2.21.0',
        'Flask==1.1.1',
        'werkzeug==0.16.1',
        'flask_cors==3.0.8',
        'flask_restplus==0.13.0'
    ]
)
