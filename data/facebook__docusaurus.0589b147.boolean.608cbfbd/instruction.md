# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX library. The build fails with an unexpected token error in the vendor file `@mdx-js__mdx@3.0.0.js`.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

// This throws an error during compilation
const result = await compile(mdxContent)
```

### Error Message

```
SyntaxError: Unexpected token 'function'
```

The error seems to be coming from the property-information module within the MDX vendor bundle. It looks like there's a malformed export statement around line 26726.

### Expected behavior

The MDX content should compile successfully without any syntax errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
