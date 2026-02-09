# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where error positions are being reported incorrectly when escape sequences are used in keywords. The error message points to the wrong location in the source code, making it difficult to identify where the actual problem is.

### Reproduction

```js
// Example MDX content with escape sequence in keyword
const mdxContent = `
import Component from './component'

// Using escape sequence in keyword (invalid)
const \u0069mport = 'test'
`

// When parsing this, the error location reported is off
// The error points to the end of the token instead of the start
```

### Expected behavior

When an escape sequence is found in a keyword, the error should point to the beginning of the keyword where the escape sequence starts, not to the end of it. This would make it much easier to locate and fix the issue in the source code.

Currently the error position seems to be pointing to the wrong character position, which is confusing when trying to debug MDX files.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
