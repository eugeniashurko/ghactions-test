import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the README file.
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dummy",
    use_scm_version={
        "relative_to": __file__,
        "write_to": "lib/version.py",
        "write_to_template": "__version__ = '{version}'\n",
    },
    description="Dummy library.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    python_requires=">=3.7",
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "numpy>=1.20.1",
        "pandas",
        "scikit-learn>=0.24.2",
        "scipy",
        "matplotlib",
        "nltk",
        "nexusforge",
        # "gensim==3.8.3",
        # "tensorflow",
        # "networkx>=2",
        # "python-louvain",
        # "tox", "pytest",
        # "pytest-bdd",
        # "pytest-cov==2.10.1",
        # "pytest-mock==3.3.1", "codecov",
        # "dash==1.19.0",
        "jupyter_dash",
        "dash_bootstrap_components",
        "dash_daq",
        "dash_extensions",
        # "dash_cytoscape",
        "nexus-sdk",
        # "pyjwt==1.7.1",
        # "ipywidgets",
        "neo4j",
        "stellargraph>=1.2.0"
    ],
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3 :: Only",
        "Natural Language :: English",
    ]
)
