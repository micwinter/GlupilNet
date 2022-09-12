from setuptools import find_packages, setup

requirements = ["numpy", "matplotlib", "torch"]

if __name__ == "__main__":
    setup(
        name="glupilnet",
        version="0.1",
        packages=find_packages(),
        install_requires=requirements,
    )
