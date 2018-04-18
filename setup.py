import os
from setuptools import setup
# https://github.com/rtfd/readthedocs.org/issues/3296
#
# I dont actually have the setup.py checked but RTD is still looking for my
# setup.py???
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    setup(
        name = "do_not_actually_install_this",
        version = "0.0.4",
        author = "No Author",
        author_email = "not-an-email@gmail.com",
        description = "This should not be installed",
        license = "BSD",
        keywords = "example documentation tutorial",
        url = "http://do.not.install/do_not_actually_install_this",
        packages=["do_not_actually_install_this"],
        long_description="This should not be installed.",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
        ],
    )
