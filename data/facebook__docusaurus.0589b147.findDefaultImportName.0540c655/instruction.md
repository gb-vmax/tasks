# Bug Report

### Describe the bug

I'm encountering an issue where default imports in MDX files are not being recognized properly. When I try to import a component using the default import syntax, the table of contents generation seems to fail to detect the import name.

### Reproduction

```mdx
---
title: My Page
---

import MyComponent from './MyComponent';

# Heading 1

<MyComponent />

## Heading 2
```

When processing this MDX file, the default import `MyComponent` is not being detected correctly, which causes issues with component resolution in the generated output.

### Expected behavior

Default imports should be properly recognized and their names should be extracted so that components can be used throughout the MDX document. The import statement `import MyComponent from './MyComponent'` should have its default import name (`MyComponent`) correctly identified.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. Previously, default imports were working fine in my MDX files.

---
Repository: /testbed
