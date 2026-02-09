# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX library. The code fails to parse/execute and throws an error about unexpected token or invalid syntax in the vendor file.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test document.
`

// This throws an error
const result = await compile(mdxSource)
```

### Expected behavior

The MDX source should compile successfully without any syntax errors. The vendor file should export the `string` property correctly from the constructs exports.

### Additional context

The issue seems to be in the `@mdx-js__mdx@3.0.0.js` vendor file around the exports section. The application was working fine before the recent changes.

---
Repository: /testbed
