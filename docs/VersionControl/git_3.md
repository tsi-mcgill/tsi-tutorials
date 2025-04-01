## About

In this tutorial we'll focus on the concept of "Continuous Integration" (CI).
CI is a process where changes made to a codebase by developers are automatically integrated and tested.
Automatic integration tools and tests are used to reduce future issues to the codebase by flagging potential errors and bugs before they are pushed to a `main` branch or, worse, a production version of the codebase.

An example of this workflow could be something like this:

1. A developer writes a section of code.
2. Upon commiting their changes, a series of tests are ran on the code.
3. If the tests are successful then the code can be pushed to the codebase.
4. If unsuccessful, the tests report helpful debugging information to help the developer resolve a potetential issue before it is commited to the codebase.
5. With the code passing tests before being merged into the `main` branch, users of the codebase can expect a greater deal of stability as mainy bugs will be caught before reaching this level.


There are many different processes that can be run as part of CI, such as:

* Testing: This is when the code is ran with a set of parameters that has a known behaviour. For example if a function f(x) has the numerical solution f(0) = 42, then the coded function function_f(0) should return 42. Anything other than 42 suggests an error in the calculation.

* Formatting: Espeically in larger codebases, it is good to stick to a consistent formatting ([tabs vs spaces](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/)), variable naming conventions ([camel vs snake vs pascal](https://khalilstemmler.com/blogs/camel-case-snake-case-pascal-case/)) and function naming convention ([Importance of naming in programming](https://wasp-lang.dev/blog/2023/10/12/on-importance-of-naming-in-programming)). By having a style guide for developers (for example [PEP 8](https://peps.python.org/pep-0008/), [Google Python Style Guide](https://android.googlesource.com/platform/external/google-styleguide/+/refs/tags/android-s-beta-2/pyguide.md)), will help with the overall readabiltiy of the code.

* Linting: [Linting](https://en.wikipedia.org/wiki/Lint_%28software%29) is the process of analyzing static code to flag potential issues such programming errors, bugs, stylistic issues. Analyzing the static code, linting can catch common issues and bugs before they are even ran. The concept of "linting" is to act as a "lint filter" to stop small bugs being propagated and causing larger issues, either performance related or more serious bugs.

* Automatic release: If there is a significant change to the code, we might want to automatically tag a new version of the code and generate a change log. This allows users to know what is the most up to date and stable version of the code. Additinoally, helps when flagging issues, as users reporting bugs can point to specific release versions of the code. 

* Automatic Building: If our code passes the required tests, we might want to automatically trigger a new build of the code. For example, if we use a container to run the code, we might want a new image (e.g. a [docker image](https://www.docker.com/)) to be build and push to a container registary (e.g. [dockerhub](https://hub.docker.com/)), allowing remote users to grab the most up to date container when they want to run the code. For Python project, we could also trigger a new version of the code to be published to [PyPi](https://www.turing.com/kb/how-to-create-pypi-packages), allowing users to install the latest version with `pip`.


In this tutorial we'll focus on three main concepts to help adapt CI principles to our codebase:

* [Commitizen](https://commitizen-tools.github.io/commitizen/) a tool for writing [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), automatic handling of versionings ([SemVer](https://semver.org/)) and automatic generation of [change logs](https://keepachangelog.com/en/1.1.0/). This encourages conforming to consistent commit messages syntax, allowing for informative change logs to be automatically generated, detailing the changes to the code.

* [Pre-commit](https://pre-commit.com/) to tool to run [git hook scripts](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) upon triggering a git action such  as committing or pushing to a remote repository. This allows for common bugs and issues to be caught before the code is even committed.

* [GitHub Actions](https://docs.github.com/en/actions/quickstart) predefined "workflows" that can be triggered by a GitHub event (e.g. `commit`, `push`, `issue`, etc). GitHub Actions will run on a virtual machine hosted by GitHub, with a large number of [pre-made actions available](https://github.com/marketplace?type=actions). These actions can range from testing to full deployment.



## Commitizen

[Commitizen](https://commitizen-tools.github.io/commitizen/) is a tool to help with writing convention commits. 
Coventional commits are human and machine readable commit messages.
These allow specific changes to be highlighted and flagged by what the specific change does.
For example, if a file (`my_file.py`) is changed to fix a bug, one might flag the commit as a `fix(my_file.py)`. 
Here we would refer to `my_file.py` as the "scope" of the change.
If a new feature is added to the code we might tag the commit with `feat(my_file.py)`. 
If the feature or fix that was implemented breaks backwards compatability, it would be good to tag this as feature breaking, this is done by adding a `!` to the end of the tag (for example `feat!(my_file.py)`).

We would then add a short comment to describe the what we have changed, for example `feat(my_file.py) adding function to do magic things`. This provides a high level description of the change. 

Finally, we might want a more descriptive commit for our records so a developer who needs a more detailed understanding can understand what changed:
```
feat(my_file.py) adding function to do magic things

The magic function is added to my_file, implementing the Houdini et al method of slight-of-handary
```

When viewing this commit on GitHub, a quicklook at the commit would see ```feat(my_file.py) adding function to do magic things```, whereas clicking on the commit one would see the full message. 
When generating the changelog, the entire message would be copied, with different commits grouped by their catagories (e.g. `feat`, `fix`, `docs` etc.).

Commitizen can be installed using `pip`:
```
pip install -U commitizen
```


We can set this up commitizen in a pre-exisiting repository using:
 