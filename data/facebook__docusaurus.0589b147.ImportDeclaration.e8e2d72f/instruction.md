# Bug Report

### Describe the bug

Import statements are being generated with incorrect syntax when using MDX. The generated code has extra commas before the first import specifier and incorrect aliasing behavior for named imports.

### Reproduction

When processing MDX files with import statements, the generated output is malformed:

```js
// Input MDX:
import { Component } from 'library'
import DefaultExport from 'other-library'

// Generated output has issues:
import , { Component as Component } from 'library'
import , DefaultExport from 'other-library'
```

The generated imports have:
1. An extra comma before the first specifier
2. Unnecessary `as` aliases even when the imported and local names are the same

### Expected behavior

Import statements should be generated with correct syntax:
- No leading comma before the first import specifier
- No `as` alias when imported name matches local name (e.g., `{ Component }` not `{ Component as Component }`)

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing syntax errors in the generated JavaScript output and breaking the build process.

---
Repository: /testbed
