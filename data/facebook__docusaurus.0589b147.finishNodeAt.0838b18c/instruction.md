# Bug Report

### Describe the bug

I'm experiencing an issue with AST node position tracking in the MDX parser. When parsing MDX content, the `end` position and `range[1]` values for AST nodes are being set incorrectly. Instead of getting numeric position offsets, they're being set to location objects, which breaks any tooling that relies on accurate position information.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test.
`

const result = await compile(mdxContent, {
  ranges: true,
  locations: true
})

// Inspect the AST nodes
console.log(result.data.estree.body[0].end) // Expected: number, Got: location object
console.log(result.data.estree.body[0].range[1]) // Expected: number, Got: location object
```

### Expected behavior

The `end` property should contain a numeric position (character offset from start of file), and `range[1]` should also be a number representing the end position. Location objects should only be stored in the `loc` property.

According to the ESTree spec, `range` should be a two-element array of numbers `[start, end]`, not location objects.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing issues with source map generation and any tools that need to extract source code based on position ranges. Any help would be appreciated!

---
Repository: /testbed
