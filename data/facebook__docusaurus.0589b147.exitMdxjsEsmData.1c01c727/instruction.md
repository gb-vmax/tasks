# Bug Report

### Describe the bug
When processing MDX files with ESM imports/exports, I'm experiencing issues with data handling in the parser. The ESM data appears to be processed incorrectly, which causes the parser to fail or produce unexpected output when dealing with import/export statements in MDX documents.

### Reproduction
```mdx
---
import { Component } from './component'
export const metadata = { title: 'Test' }
---

# My Document

<Component />
```

When parsing this MDX file, the ESM data (imports/exports) is not being handled correctly. The parser seems to be calling the wrong context or skipping necessary processing steps for ESM data tokens.

### Expected behavior
The parser should correctly process both the entry and exit of ESM data tokens, maintaining proper context throughout the parsing lifecycle. Import and export statements should be parsed without errors and the resulting AST should be valid.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
