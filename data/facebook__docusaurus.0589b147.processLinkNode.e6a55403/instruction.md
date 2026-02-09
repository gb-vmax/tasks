# Bug Report

### Describe the bug

Links with `@site/` alias or asset-like file extensions (images, PDFs, etc.) are being incorrectly processed by the MDX loader. These links should be left as-is but are currently being transformed, which breaks the linking behavior.

### Reproduction

```md
<!-- This link gets incorrectly transformed -->
[Download PDF](@site/static/files/document.pdf)

<!-- This image link also gets incorrectly transformed -->
![Logo](@site/static/images/logo.png)

<!-- Asset links without @site alias are also affected -->
[Image](./assets/photo.jpg)
```

When these links are used in MDX files, they don't resolve correctly. The `@site/` aliased paths and paths to asset files (with extensions like `.pdf`, `.png`, `.jpg`, etc.) should not be transformed by the link transformer.

### Expected behavior

Links with `@site/` alias should be preserved as-is without transformation. Similarly, links pointing to asset files (files with extensions other than `.md`, `.mdx`, or `.html`) should also be left untouched.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
