# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX compiler. The error indicates there's a malformed export statement in the vendor file for `@mdx-js/mdx@3.0.0`.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test MDX document.
`

// This throws a syntax error
const result = await compile(mdxSource)
```

### Error Message

```
SyntaxError: Unexpected token 'function'
```

The error seems to be coming from the vendored MDX library file. It looks like there's an issue with how the `number` export is defined in the types module - there's a function declaration where there should be a simple export.

### Expected behavior

The MDX compiler should work without syntax errors. The `number` type should be properly exported from the types module.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
