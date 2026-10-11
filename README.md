# Garifuna Repository (GitHub Pages)

Static, read-only site. No accounts, no server, no service worker.

## Files
- `index.html`: the whole site. Pages are `#/article`, `#/timeline`, `#/sources`, `#/glossary`, `#/quiz`, `#/about`, `#/news`, `#/library`, `#/tools`, `#/principles`.
- `assets/css/site.css`, `assets/js/app-*.js`: styles and scripts (all linked with relative paths).
- `src/site.html` + `build.py`: editable single-file source and the script that regenerates `index.html` and `assets/`.

## Publish
Upload everything to a GitHub repo and enable Settings > Pages > Deploy from branch. It works at a user/domain root or under a project sub-path such as `https://user.github.io/repo/`.

## Edit
Change `src/site.html`, run `python3 build.py`, commit the result.
