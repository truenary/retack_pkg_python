from setuptools import setup, find_packages

setup(
    name="retack-sdk-django",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[],
    author="Truenary Solution",
    author_email="contact@truenary.com",
    description="An error tracking tool.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/truenary/retack_pkg_python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)