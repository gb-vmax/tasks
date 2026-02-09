# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where comments in ESM blocks are not being properly attached to the AST. When using `mdxjsEsm` with code that contains comments, the comments array appears to be `undefined` in certain cases, which causes the spread operator to fail.

### Reproduction

```js
// MDX file with ESM block containing comments
const mdxContent = `
import { something } from 'somewhere'
// This is a comment
export const value = 42
`

// Parse the MDX
const result = compile(mdxContent)
```

When the estree data doesn't include a comments array (or it's undefined), the code tries to spread `undefined` which causes issues with comment handling.

### Expected behavior

The parser should gracefully handle cases where the comments array is missing or undefined, and comments should be properly attached to the estree before being added to the state.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
