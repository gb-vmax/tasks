# Bug Report

### Describe the bug

Images referenced with `@site/` alias are not resolving correctly. When I use `@site/static/img/logo.png` in my markdown files, the build fails with an error saying the image file cannot be found, even though the file definitely exists at that path.

### Reproduction

1. Create a markdown file with an image reference using `@site/` alias:
```md
![Logo](@site/static/img/logo.png)
```

2. Place the actual image file at `static/img/logo.png` in your site directory

3. Build the site

The build fails with an error about the image not being found.

### Expected behavior

The `@site/` alias should correctly resolve to the site root directory and find the image file. This was working fine before but seems to have broken recently.

### Additional context

This appears to affect all images using the `@site/` prefix. Using relative paths works as a workaround, but the `@site/` alias is much more convenient for referencing static assets.

---
Repository: /testbed
