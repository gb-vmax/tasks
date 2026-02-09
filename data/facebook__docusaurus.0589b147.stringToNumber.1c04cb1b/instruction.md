# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the MDX parser. It seems like there's corrupted code in the vendor bundle that's preventing the parser from functioning at all.

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

### Expected behavior

The MDX content should compile successfully without any syntax errors. The parser should be able to process basic MDX documents.

### Actual behavior

Getting a syntax error that appears to be coming from the vendored MDX code itself. The error suggests there's invalid JavaScript in the bundle - looks like actual code got replaced with numbers or something?

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking our entire build process. Any help would be appreciated!

---
Repository: /testbed
