import setuptools
import version

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="mlopspython-extraction",
    version=version.VERSION,
    packages=["extraction"],
    package_dir={"": "src"},
    package_data={"extraction": ["*"]},
    install_requires=requirements,
    author="Guillaume Chervet",
    include_package_data=True,
    python_requires=">=3.8",
    author_email="guillaume.chervet@gmail.com",
    url='https://github.com/guillaume-chervet/MLOpsPython',
    description="Inference package for MLOpsPython project",
    long_description="Inference package for MLOpsPython project",
    platforms='POSIX',
    classifiers=["Programming Language :: Python :: 3 :: Only",
                 "Programming Language :: Python :: 3.11",
                 ]
)
