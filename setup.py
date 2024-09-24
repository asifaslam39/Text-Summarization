import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version___="0.0.0"

REPO_NAME="Text-Summarization"
AUTHOR_USERNAME="asifaslam39"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="asifaslam19082@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version___,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python Package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",},
     package_dir={"":"src"},
     packages=setuptools.find_packages(where="src")   
    
)
