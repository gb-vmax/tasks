# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM (import/export) parsing. When processing MDX files with ESM blocks, the parser seems to be creating nodes with an incorrect type identifier.

### Reproduction

```js
// Parse an MDX file with ESM imports
const mdx = `
import { Component } from './component'

# Hello World
`

// Process the MDX
const result = await compile(mdx)
// The ESM node type is wrong in the AST
```

When I inspect the resulting AST, the ESM import nodes have type `"mdxjsEsmValue"` instead of the expected `"mdxjsEsm"`. This breaks any tooling or plugins that rely on identifying ESM nodes by their type.

### Expected behavior

ESM import/export blocks should be represented as nodes with type `"mdxjsEsm"` in the syntax tree, not `"mdxjsEsmValue"`. The node value should be an empty string initially, not `undefined`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing issues with my custom remark plugins that need to traverse and identify ESM nodes in the MDX AST. Any workarounds or fixes would be appreciated!

---
Repository: /testbed
