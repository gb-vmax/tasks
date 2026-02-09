# Bug Report

### Describe the bug

Images with relative paths in MDX files are not resolving correctly. When using a relative image path like `./image.png` or `../assets/logo.png`, the image fails to load or shows a broken link.

### Reproduction

Create an MDX file at `docs/guides/tutorial.mdx` with a relative image reference:

```mdx
# My Tutorial

![Example](./example.png)
```

Place `example.png` in the same directory as the MDX file (`docs/guides/`).

The image doesn't display and the path resolution appears to be incorrect.

### Expected behavior

Relative image paths should be resolved against the MDX file's directory, so `./example.png` should correctly point to `docs/guides/example.png`.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
