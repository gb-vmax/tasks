# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where ESM import/export statements are not being processed correctly. The parser seems to be calling methods in the wrong order or with incorrect context, which causes the data to not be properly extracted from ESM blocks.

### Reproduction

```js
const mdxContent = `
import { Component } from './Component'

export const metadata = { title: 'Test' }

# Hello World
`

// Parse the MDX content
const result = parseMDX(mdxContent)

// The ESM data is malformed or missing
console.log(result.imports) // undefined or incorrect
```

### Expected behavior

ESM imports and exports in MDX files should be correctly parsed and accessible in the resulting AST. The data should be properly entered and exited during the parsing process.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
