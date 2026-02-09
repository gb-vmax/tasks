# Bug Report

### Describe the bug

When importing MDX files using default imports in Docusaurus, the import name is not being detected correctly. This affects the table of contents generation and potentially other features that rely on parsing MDX imports.

### Reproduction

```mdx
---
title: My Page
---

import MyComponent from './MyComponent';

<MyComponent />
```

The default import `MyComponent` is not being recognized properly, which can cause issues with MDX processing and component resolution.

### Expected behavior

Default imports should be correctly identified and their names should be extracted for use in TOC generation and other MDX processing features. The import declaration parser should properly distinguish between default imports (`ImportDefaultSpecifier`) and named imports (`ImportSpecifier`).

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The MDX loader appears to be looking for the wrong type of import specifier when trying to find default import names.

---
Repository: /testbed
