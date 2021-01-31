import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jasper-rest-client",
    version="0.0.1",
    author="Marco Castro",
    author_email="marcotc.al@gmail.com",
    description="JasperReports REST client",
    url="https://github.com/marcotcal/jasper-rest-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)