import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

package_data = {
    '': [
        './templates/*.html',
    ]
}

setuptools.setup(
    name="roughviz",
    version="4.7.0",
    author="Hannan Satopay",
    author_email="sathannan@hotmail.com",
    description="A python visualization library for creating sketchy/hand-drawn styled charts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/hannansatopay/roughviz",
    packages=setuptools.find_packages(),
    install_requires=['Jinja2','pandas'],
    package_data=package_data,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: IPython",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
