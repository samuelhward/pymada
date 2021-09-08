import setuptools, pathlib

setuptools.setup(
    name="pymada",
    version="0.0.1",
    packages=["pymada"],
    url="https://github.com/armoured-moose/pymada",
    author="Samuel Ward",
    author_email="samuelhward@gmail.com",
    description="SW Armada AI project",
    long_description=open(
        pathlib.Path(__file__).parents[0] / "docs" / "README.md"
    ).read(),
    install_requires=[
        "attrs==20.3.0",
        "bokeh==2.3.0",
        "iniconfig==1.1.1",
        "Jinja2==2.11.3",
        "MarkupSafe==1.1.1",
        "numpy==1.20.2",
        "packaging==20.9",
        "Pillow==8.3.2",
        "pluggy==0.13.1",
        "py==1.10.0",
        "pyparsing==2.4.7",
        "pytest==6.2.3",
        "python-dateutil==2.8.1",
        "PyYAML==5.4.1",
        "six==1.15.0",
        "toml==0.10.2",
        "tornado==6.1",
        "typing-extensions==3.7.4",
    ],
)