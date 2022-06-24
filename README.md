# automation-base-repo

This will be the base repo for all future automation tasks.

# What is this?

Why spend time reviewing code for syntax errors and checking file size errors etc.? Why not let the system do this?

This repository contains the base to get you started with git hooks and to push all the basick check onto the system. These hooks will not allow you to commit to the repo unless all the issues are fixed.

# Setup

1.  Clone the repo.

        git clone https://gitlab.com/vinayNaik/python-pre-commit-base.git

2.  Install the dependencies

        //For Python2.7
        pip install pre-commit

        //For Python3
        pip3 install pre-commit

        //For anaconda python environment
        conda install -c conda-forge pre_commit

3.  Initialize the git hook

        pre-commit install

4.  To update the hooks with the latest hook dependencies run

        pre-commit autoupdate

5.  To run on all files

        pre-commit run --all-files

# Use Pipenv to manage pakages and dependencies

> **Important**
>
> Regularly update the hooks. But do note that some updates might break the hook. In this case revert that particular hook to the previous version by updating the **rev** key for that hook in the **.pre-commit-config.yaml** file.

---

# Example

## Pre commit failure

![Sample pre commit](/assets/images/sample_pre_commit_failure.png "Pre commit hook failure.")

## Pre commit success

![Sample pre commit](/assets/images/sample_pre_commit_success.png "Pre commit hook success.")
