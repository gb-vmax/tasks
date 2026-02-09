# Bug Report

### Describe the bug

When parsing MDX files with ESM imports/exports, the `mdxjsEsm` nodes are being created without a `value` property initialized, and the parser is calling `resume()` instead of `buffer()` on entry. This causes the ESM content to not be properly captured.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
export const foo = 'bar'

# Hello World
`

const result = await compile(mdxContent)
// The ESM export is not being captured correctly in the AST
```

### Expected behavior

The `mdxjsEsm` nodes should have their `value` property properly initialized as an empty string, and the parser should call `buffer()` when entering the ESM block to start capturing the content. The `resume()` call should only happen on exit to retrieve the buffered content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
