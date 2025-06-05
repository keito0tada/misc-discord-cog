from setuptools import find_packages, setup

setup(
    name="misc_cog",
    version="0.1.0",
    author="Keito Tada",
    packages=find_packages(),
    install_requires=["discord"],
    include_package_data=True,
)
