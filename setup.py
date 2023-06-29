import setuptools 

with open("README.md", "r", encoding="utf8") as f:
    long_description  =f.read()


__version__ = "0.0.0"
REPO_NAME = "ANN-Implementation"
AUTHOR_USER_NAME = "ShreyasRkk"
SRC_REPO = "ANN-Implementation"
AUTHOR_EMAIL = "shreyasrk64@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "ANN Implementation",
    long_description= long_description,
    long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        packages = ["src"],
        python_requires = ">=3.7"
        
)
