import setuptools

#in your requirements.txt add -e .
#to download other files as part of
#your setup package
#-e . allows you to install the setup.py file

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "end-to-end-machine-learning-project-with-mlflow"
AUTHOR_USER_NAME = "ny-essien"
SRC_REPO = "mlproject"  
AUTHOR_EMAIL = "nsikan4001@gmail.com"

setuptools.setup(

    name = SRC_REPO,
    version = __version__,
    author_email= AUTHOR_EMAIL,
    description = "A python package for a machine learning app",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {

        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where="src")
)