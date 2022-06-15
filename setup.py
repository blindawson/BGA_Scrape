from setuptools import setup, find_packages

setup(
    name="BGA_Scrape",
    version="0.1",
    author="Brian Lindawson",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "bs4",
        "selenium",
        "webdriver_manager",
    ],
    extras_require={"dev": ["pytest", "black"]},
    python_requires=">=3.9",
)