# Bruna Campos Guedes — Academic Website

Source code for my personal academic website: **[brunacg.github.io](https://brunacg.github.io/)**.

The site presents my research in machine learning, relational learning, graph neural networks, and reliable AI for healthcare, together with selected publications, academic experience, and research profiles.

## Site structure

```text
.
├── index.html              # Main one-page academic website
├── 404.html                # Custom GitHub Pages 404 page
├── favicon.svg             # Main browser icon
├── favicon-32x32.png       # PNG browser icon fallback
├── apple-touch-icon.png    # iOS home-screen icon
├── og-preview.png          # Open Graph / social sharing preview
├── site.webmanifest        # Web app metadata
├── robots.txt              # Search engine crawling rules
├── sitemap.xml             # Search engine sitemap
├── .nojekyll               # Serve the repository as plain static files
├── .gitignore              # Local/editor files excluded from Git
├── LICENSE                 # License for the website source code
└── README.md
```

## Technology

This is a static GitHub Pages website with no build step. It uses:

- HTML5 and custom CSS
- Bootstrap 4.6.2 via CDN
- Font Awesome 5.15.4 via CDN
- Google Fonts (Inter and Source Serif 4)
- a small amount of JavaScript for responsive navigation

The repository intentionally contains only files used by the current production website. Legacy template assets, unused portfolio images, SCSS sources, npm/gulp tooling, and local copies of third-party libraries have been removed.

## Local preview

From the repository root:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000` in a browser.

You can also open `index.html` directly, although using a local HTTP server is preferable for testing root-relative assets and metadata.

## Deployment

The site is hosted with GitHub Pages from the root of this repository. Updating the default branch updates the website automatically according to the repository's Pages configuration.

## Academic profiles

- [ORCID](https://orcid.org/0000-0002-4384-0056)
- [Google Scholar](https://scholar.google.com/citations?user=6fiZEtUAAAAJ&hl=en)
- [Lattes](http://lattes.cnpq.br/5098861497873665)
- [GitHub](https://github.com/brunacg)
- [LinkedIn](https://www.linkedin.com/in/brunacamposguedes/)

## Credits and license

The current site is substantially customized from the original **Start Bootstrap Agency** design. Bootstrap, Font Awesome, Google Fonts, and other third-party resources retain their respective licenses.

The website **source code** in this repository is available under the [MIT License](LICENSE). Personal biographical content, research descriptions, publication metadata, CV content, and other authored academic material remain © Bruna Campos Guedes unless otherwise stated.
