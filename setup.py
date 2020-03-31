import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywebchat",
    version="0.0.1",
    author="han-solo",
    author_email="hanish0019@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
	'starlette',
        'python-socketio',
        'uvicorn',
        'aiofiles',
        'Jinja2',

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "pywebchat = pywebchat.__main__:main",
        ],},
)
