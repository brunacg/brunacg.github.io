# Replacing the old repository files

This folder is the complete production website.

## Safest replacement workflow

1. Make a backup or create a Git branch before deleting anything.
2. In the existing `brunacg.github.io` working directory, keep the hidden `.git/` directory.
3. Delete the old website files and folders from the working tree (do **not** delete `.git/`).
4. Copy every file from this clean package into the repository root.
5. Preview locally with:

   ```bash
   python -m http.server 8000
   ```

6. Verify the homepage, mobile menu, external links, DOI links, icons, favicon, and 404 page.
7. Commit all deletions and additions together.

Example:

```bash
git checkout -b cleanup/website-repository
git status
git add -A
git commit -m "Clean up academic website repository"
git push -u origin cleanup/website-repository
```

If you prefer to update the default branch directly, omit the branch step.

## Important

The package intentionally replaces the old `vendor/`, `img/`, `scss/`, `mail/`, `css/`, and `js/` template folders. The production site now uses pinned CDN versions of Bootstrap and Font Awesome, while all site-specific styling is contained in `index.html`.
