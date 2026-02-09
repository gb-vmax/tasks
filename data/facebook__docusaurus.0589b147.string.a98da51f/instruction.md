# Bug Report

### Describe the bug

I'm getting a syntax error when trying to use the MDX parser. It looks like there's an issue with the exported constructs from the `@mdx-js/mdx` package. The code is failing to parse even simple MDX content.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This throws an error
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without any syntax errors. The parser should be able to handle basic markdown content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

The error message suggests there's something wrong with the module exports, but I can't figure out what's causing it. This was working fine in the previous version.

---
Repository: /testbed
