from setuptools import setup, find_packages

setup(
    name="tenet-tracker",
    version="0.0.1",
    description="Tracks completion of tenets",
    author="Zachary Abresch",
    author_email="zachary.abresch@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["tenet-tracker = tenet_tracker.__main__:main",]},
)
