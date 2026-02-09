# Bug Report

### Describe the bug

I'm experiencing an issue with the TOC (Table of Contents) generation in my Docusaurus project. After a recent update, the import declarations are not being properly extracted from MDX files, which is causing the TOC to fail to render correctly or throw errors during build.

### Reproduction

Create an MDX file with import statements:

```mdx
---
title: My Page
---

import MyComponent from './MyComponent';
import { Something } from './utils';

# Heading 1

Some content here

## Heading 2

More content
```

When this file is processed, the TOC generation seems to fail or behave unexpectedly. The imports should be recognized and filtered properly, but something appears to be broken in how they're being extracted from the AST.

### Expected behavior

The MDX loader should correctly identify and extract import declarations from the file's AST, allowing the TOC to be generated properly without errors. Import statements should not interfere with heading extraction.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- Operating System: macOS

---
Repository: /testbed
