import setuptools
from pathlib import Path

README_FILE = Path(__file__).parent / "README.md"


def main():
    long_description = README_FILE.read_text()

    setuptools.setup(
        name="BodyCompositionScale2",
        version="1.0.0",
        author="Dennis89",
        author_email="straub.dennis1@web.de",
        description="A library to read the Body Composition Scale 2 without App",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/Dennis-89/BodyCompositionScale2.git",
        packages=setuptools.find_packages(),
        install_requires=["bluepy"],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
            "Operating System :: POSIX :: Linux",
            "Topic :: System :: Hardware",
        ],
    )


if __name__ == "__main__":
    main()