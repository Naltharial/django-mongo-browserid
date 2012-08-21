from distutils.core import setup

setup(
    name='django-mongo-browserid',
    description='Django application for adding BrowserID support with MongoEngine backend.',
    version='0.1',
    packages=['django_mongo_browserid', 'django_mongo_browserid.tests'],
    author='Paul Osman, Michael Kelly. Primoz Jeras',
    author_email='normandyh@gmail.com',
    url='https://github.com/Naltharial/django-mongo-browserid',
    license=open("LICENSE").read(),
    install_requires='requests>=0.9.1',
    package_data={'django_mongo_browserid': ['static/browserid/*.js']},
)
