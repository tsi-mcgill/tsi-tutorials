# Introduction

This repo contains various tutorials that have been delivered for the TSI. For simplicity, we're using [MkDocs](https://www.mkdocs.org/) to generate a website that is hosted on GitHub Pages. The website is live here:  
[https://tsi-mcgill.github.io/tsi-tutorials/](https://tsi-mcgill.github.io/tsi-tutorials/)

## Building the Website

When developing the website, you can use MkDocs to create a development server using:

```
mkdocs serve --dev-addr localhost:8001
```

Here we're explicitly launching a dev server at the address localhost:8001. This can be changed as needed.

To build and deploy the website, simply run:

```
mkdocs gh-deploy
```
If you'd like to host the website using a different method, you can first build the website using:
```
mkdocs build
```
to generate the `site` folder.
