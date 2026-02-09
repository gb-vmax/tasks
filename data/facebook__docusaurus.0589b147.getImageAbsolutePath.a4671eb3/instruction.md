# Bug Report

### Describe the bug

Images with relative paths in MDX files are not resolving correctly. When I use a relative image path like `./image.png` or `../assets/logo.png` in my MDX content, the images fail to load. 

Additionally, images using the `@site/` alias seem to be broken as well. The `@site/` prefix isn't being stripped properly before the path is resolved.

### Reproduction

In an MDX file located at `docs/guides/tutorial.mdx`:

```md
# My Tutorial

![Local image](./screenshot.png)
![Asset image](../assets/logo.png)
![Site alias](@site/static/img/banner.png)
```

All three image references fail to resolve. The browser shows 404 errors for these images even though the files exist in the correct locations.

### Expected behavior

- Relative paths like `./screenshot.png` should resolve relative to the MDX file's directory
- Parent directory paths like `../assets/logo.png` should work correctly
- The `@site/` alias should be properly replaced with the site directory path and images should load

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
