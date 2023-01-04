import setuptools

setuptools.setup(
    name="redfid_logout",
    version="0.0.1",
    author="Luis Santana",
    author_email="luis.santana@uchile.cl",
    description=".",
    url="https://eol.uchile.cl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "lms.djangoapp": ["redfid_logout = redfid_logout.apps:RedfidLogoutConfig"],
        "cms.djangoapp": ["redfid_logout = redfid_logout.apps:RedfidLogoutConfig"]
    },
)
