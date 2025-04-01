## Introduction

Welcome to this workshop where we'll explore the use of [MkDocs](https://www.mkdocs.org/) to build your own personal website. MkDocs, a Python package, streamlines the process by allowing you to focus on creating content in [Markdown](https://en.wikipedia.org/wiki/Markdown) – a highly human-readable language. This eliminates the need to delve into HTML, JavaScript, or other web development languages. Originally designed for documentation, MkDocs offers a swift and intuitive solution for crafting a personalized website.


## Requirements

In this workshop, we'll assume that you have a Python package manager. If you don't already have one set up, I recommend installing [mamba](https://mamba.readthedocs.io/en/latest/). Mamba is designed to be a "drop-in replacement for conda," meaning you can substitute any conda commands for mamba. For example:


```bash
conda install numpy
```
Becomes
```bash
mamba install numpy
```

And so on. 


We'll be using the following packages. Installing them prior to the workshop will help you follow along:
```
mkdocs
mkdocs-material
mkdocstrings
mkdocstrings-python
mkdocs-jupyter
```

To create a new working environment and install these packages run:
``` bash
mamba create -n website-workshop python=3.11 mkdocs mkdocs-material mkdocstrings mkdocstrings-python mkdocs-jupyter
```

Substituting mamba for conda if you're running with conda.

You can activate this environment with:
```bash
mamba activate website-workshop
```


## About MkDocs

MkDocs provides a convenient method for creating quick static websites. Originally designed to generate documentation for code packages, learning how to utilize MkDocs offers the added benefit of generating documentation pages for your own coding projects.

For instance, [this tutorial](https://realpython.com/python-project-documentation-with-mkdocs/) demonstrates how to use MkDocs to generate documentation from Python docstrings. This process combines the steps of properly commenting on one's code with providing future users accessible documentation, all in a single, simple step that can be run as a pre-commit step.


## Creating a new project

With MkDocs we can create a new project using the following command:
```bash
mkdocs new project-name
```
Alternatively, we can initialize MkDocs for an existing project using:
```bash
mkdocs init .
```

This will create the following files:
```
╰─➤  tree
.
├── docs
│   └── index.md
└── mkdocs.yml
```

The `mkdocs.yml` file is the configuration file for MkDocs. At the moment it will just contain the `site_name`.

```yaml
site_name: My Docs
```
The website will appear with the "My Docs" title.

The `docs` folder is where we'll write all our pages in Markdown. Inside this folder, we have the file `index.md`, which serves as a placeholder page.


## Launching a test server

We've created a new project. To preview our webpage, we can launch a test server with the following command:
```bash
mkdocs serve
```
We can now view our webpage by navigating to `127.0.0.1:8000` or `localhost:8000` in our browser. If the `8000` port is in use, you can specify a different port using:


```bash
mkdocs serve -a localhost:8001
```

## Website Layout

Looking at `docs/index.md`, we see that this is our "home page." We can add new pages as new `.md` files. Any `.md` files within the `docs` folder or subfolders will be rendered to HTML. For example, if we create a file `about/about.md` to contain a small about section, it will be rendered to `website.com/about/about/`. Alternatively, using `about/index.md` will render the page to `website.com/about`.

## Creating a navigation bar

A navigation bar can be managed from the `mkdocs.yml` file. This is handled in the `nav` section of the environment file:

```
# For describing the navigation panel
nav:
  - Home: index.md
  - About Me: about/index.md
  - Research: reasearch/index.md
  - Projects: projects/index.md
```

This links the `index.md` page to "Home," `about/index.md` to "About Me," `research/index.md` to "Research," and `projects/index.md` to "Projects." This will appear as:

![Example of Navigation](./images/website_header.png)


## Example File Layout

Here is an example file layout. Note that each project or subsection contains its own folder, with its own `.md` file, and, when appropriate, its own `media` folder (for images, videos, etc.). Separating each project into a separate folder will help to better organize and compartmentalize individual projects.


```
├── docs
│   ├── about
│   │   ├── cooking.md
│   │   ├── cycling.md
│   │   ├── fishing.md
│   │   └── index.md
│   ├── index.md
│   ├── media
│   │   └── Crab_Nebula.jpg
│   ├── projects
│   │   ├── data_project
│   │   │   ├── index.md
│   │   │   └── media
│   │   │       └── example.csv
│   │   ├── index.md
│   │   └── python_project
│   │       └── python_project.ipynb
│   └── reasearch
│       ├── all_publications.md
│       ├── highlights
│       │   ├── awesome_paper
│       │   │   ├── index.md
│       │   │   └── media
│       │   │       └── einstein.png
│       │   └── large_mwl_paper
│       │       ├── index.md
│       │       └── media
│       │           └── coma_cluster.png
│       └── index.md
├── javascripts
│   └── mathjax.js
├── mkdocs.yml

```

## Adding Media

Media, such as images, can be included using the following syntax:

```
![Name of image](./path/to/image.png)
```
The image path is a relative path, but can also link to a web-hosted image. 

Links can be added using a similar syntax, with the `!` removed:
```
[Text to display](www.website.com)
```
or
```
[Internal Link](./path/to/internal/page.md)
```

Images and be aligned and resized using something like:
```
![Image name](./path/to/image.png){align="left": style="height:150;width:150px"} 
```
This will align the image to the left of the page and resize the image to be 150x150 pixels (px). 

This requires the following additions to the `mkdocs.yml` file:
```yaml
...
markdown_extensions:
  ...
  - attr_list   # For adding attributes such as right/left align to images
  - md_in_html  # Using Figures
  ...
```

`md_in_html` allows us to wrap images in "figures" (similar to $\LaTeX$ figures), which provides centering and captions:

```
<figure markdown>
  ![Image Name](./path/to/image.png){: style="height:300px;width:500px"}
  <!-- Within fig caption normal markdown linking doesn't work, instead use a href attribute -->
  <figcaption>Centered and resized image of the Coma Cluster (source <a href="https://esahubble.org/images/potw1849a/">ESA</a>) </figcaption>
</figure>
```


## Rendering Latex

$\LaTeX$ equations can be rendered inline (`$ equation $`) or in display mode (`$$ equation $$`). To enable this rendering, we'll use a small bit of JavaScript. Add the file `mathjax.js`:

```javascript
    window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
  
  document$.subscribe(() => { 
    MathJax.typesetPromise()
  })
  
```
Create a `javascripts` directory in the project directory. Additionally, add the following to the `mkdocs.yml` file:

```
extra_javascript:
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

Where `mathjax.js` is located at `project/javascripts/mathjax.js`.

## Including a Bibliography
Using the `bibtex` plugin and the `footnote` Markdown extension, one can use citations throughout the website. Ensure you have `mkdocs-bibtex` and `pandoc` installed.

```
pip install mkdocs-bibtex
mamba install pandoc
```

Adding the following sections to our `mkdocs.yml` file:

```
plugins:
    ...
    - bibtex:
        bib_file: "/path/to/bibtex.bib"
        # Optional
        csl_file: "/path/to/harvard-cite-them-right-10th-edition.csl"
    ...

...

markdown_extensions:
  ...
  - footnotes

```

This assumes we have a `.bib` file somewhere accessible to our project. Optionally, a `csl_file` can be specified (CSL = Citation Style Language). CSL files can be found [here](https://github.com/citation-style-language/styles).

Assuming we have an entry in our `.bib` file like:
```
@ARTICLE{2024ApJ...960...75P,
...
}
```
We can cite this anywhere on our website using:
```
(remove the "\")
[@\2024ApJ...960...75P]
```

This will render a citation like $\rightarrow$ [@2024ApJ...960...75P], with the reference appearing at the bottom of the page as a footnote.

The entire contents of a `.bib` file can be displayed with the `[\]full_bibliography` command (remove the `[]`). Note: I've found that I need to have at least 1 citation somewhere within the website in order for the entire bibliography to render.


## Deploying Website

### Deploying to physics.mcgill.ca

Anyone with an account on the physics.mcgill.ca cluster can host a website at physics.mcgill.ca/~username. To do this, connect to the cluster and clone the GitHub repo onto the machine. Build the webpage using:

```
mkdocs build
```
This produces a folder called `site`. Copy the contents of this folder to `~/WWW/`. "Push" this to the web server using:

```
ssh -x www.hep webpush
```
After a few moments, the updated website will be available at `physics.mcgill.ca/~your_username/`. If you copied the directory to something like `~/WWW/awesome/`, then the page will appear at `physics.mcgill.ca/~your_username/awesome/`.

### Deploying to GitHub Pages
Every GitHub account has access to a "GitHub Pages" domain. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) is a static site hosting service. We can deploy to GitHub Pages from MkDocs by simply running:

```
mkdocs gh-deploy
```

This renders the markdown to HTML and creates a new branch called `gh-pages`. 


After a few moments, the page will be rendered at `https://github_username.github.io/repo_name/`.
For example [https://tsi-mcgill.github.io/website-template/](https://tsi-mcgill.github.io/website-template/). You can access this template on GitHub ([see https://github.com/tsi-mcgill/website-template](https://github.com/tsi-mcgill/website-template)).

If you are cloning an existing template, be sure to create a new repo on `GitHub` and add this repo as the remote origin. For example:
```
git clone git@github.com:tsi-mcgill/website-template.git
mv website-template website-example
cd website-example
git remote set-url origin git@github.com:steob92/website-example.git
```

Alternatively click on the "Use this template" dropdown menu and follow the instructions.
![Use this template](./images/use_template.png)

The GitHub Page can be managed from the Settings of the GitHub repo.
![Settings example](./images/gh-pages-settings.png)


## Themes

MkDocs has many supported themes to allow for customization to one's desire. Changing the theme is handled from the `mkdocs.yml` file. See [here](https://www.mkdocs.org/user-guide/choosing-your-theme/) for examples of how to change the theme and [here](https://github.com/mkdocs/catalog#-theming) for a list of popular third-party themes.
