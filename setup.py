import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="gptprobe",
    version="0.0.5",
    description="Probing chatgpt",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gptprobe/gptprobe",
    author="gptprobe",
    author_email="pcotton@intechinvestments.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["gptprobe","gptprobe.openaiwrappers","gptprobe.utilfortests","gptprobe.parsing"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["numpy","pandas","getjson","openai"],
    entry_points={
        "console_scripts": [
            "gptprobe=gptprobe.__main__:main",
        ]
    },
)
