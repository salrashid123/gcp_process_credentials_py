import setuptools
import io
import os


package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, 'README.md')
with io.open(readme_filename, encoding='utf-8') as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name="gcp_process_credentials",
    version="0.0.1",
    author="Sal Rashid",
    author_email="salrashid123@gmail.com",
    description="Python ProcessCredentials for Google Cloud Platform",
    long_description=readme,
    url="https://github.com/salrashid123/gcp_process_credentials_py",
    install_requires=[
          'google-auth',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        "Programming Language :: Python",
        "Programming Language :: Python :: 3.0",

        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
