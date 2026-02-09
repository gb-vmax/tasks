# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX compiler. It looks like there's some invalid JavaScript in the vendor bundle that's preventing the code from parsing correctly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test document.
`

// This throws a syntax error
const result = await compile(mdxSource)
```

### Error Message

The code fails to parse with a syntax error. It seems like there's TypeScript syntax or a function declaration in the middle of an export statement where it shouldn't be.

### Expected behavior

The MDX compiler should work without syntax errors and successfully compile the MDX source.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
