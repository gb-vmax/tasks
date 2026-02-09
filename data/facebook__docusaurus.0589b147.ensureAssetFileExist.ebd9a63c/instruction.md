# Bug Report

### Describe the bug

When referencing local assets (images, files, etc.) in MDX files, I'm getting an error saying the asset is not found even though the file definitely exists in my project. The error message is confusing because it shows the wrong file path.

### Reproduction

1. Create an MDX file at `docs/my-page.mdx`
2. Add a reference to a local image that exists: `![alt text](./images/screenshot.png)`
3. Make sure the image file actually exists at `docs/images/screenshot.png`
4. Build the project

The build fails with an error like:
```
Asset docs/my-page.mdx used in docs/my-page.mdx not found.
```

This doesn't make sense - the error is saying the MDX file itself is not found, when it should be checking for the image file.

### Expected behavior

The build should succeed since the asset file exists. Or if there's actually a missing file, the error message should correctly identify which asset is missing, not reference the source MDX file.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
