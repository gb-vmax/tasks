# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where import/export statements with multiple consecutive spaces are not being handled correctly. The parser seems to be consuming spaces as part of the keyword buffer instead of treating them as separators.

### Reproduction

```js
// This works fine
import { something } from 'module'

// This fails to parse correctly
import  { something } from 'module'  // note the double space after 'import'

// Same issue with export
export  const value = 123  // double space after 'export'
```

When there are multiple spaces between the `import`/`export` keyword and the rest of the statement, the parser doesn't recognize it as a valid ESM statement.

### Expected behavior

The parser should handle any amount of whitespace (single or multiple spaces) between the import/export keyword and the following tokens, just like JavaScript does.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
