from setuptools import setup, find_packages

setup(
    name = "Python_Utilities",
    version = "1.2.1",
    packages = find_packages(where = "src"),
    package_dir = {"": "src"},

    author = "Golden Dev",
    author_email = "miguizin.10@gmail.com",
    description = "Utilities for annoying or slowing details, like capitalizing booleans"
)