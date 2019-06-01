from setuptools import setup

def read(filename):
    with open(filename) as f:
        return f.read()

setup(
    name='django-minio-wrapper',
    version='0.1',
    py_modules=['django_minio_wrapper'],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=['minio', 'django-minio-storage'],
    author='Davide Depau',
    author_email='davide@depau.eu',
    license='MIT',
    description='Wraps Django Minio storage so it can be initialized with JSON data',
    url='https://github.com/Depau/django-minio-wrapper',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
