import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiocleverbot",
    version="0.1.1",
    author="Johan Naizu",
    author_email="johan@naizu.in",
    description="Async library for cleverbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johan-naizu/aiocleverbot",
    project_urls={
        "Bug Tracker": "https://github.com/johan-naizu/aiocleverbot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
