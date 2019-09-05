from setuptools import setup

setup(
    name="servercheck",
    version="0.1",
    packages=["ServerCheck"],
    install_requires=[
        "psutil",
        "click",
        "requests",
        "asyncio"
    ],
    entry_points={
        "console_scripts": [
            "ServerCheck = ServerCheck.cli:cli"
        ]
    },
)
