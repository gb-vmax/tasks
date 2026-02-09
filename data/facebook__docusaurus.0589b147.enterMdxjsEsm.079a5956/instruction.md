# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM imports parsing. When processing MDX files that contain ESM import/export statements, the parser is generating incorrect AST nodes. Instead of creating `mdxjsEsm` type nodes as expected, it's creating `mdxFlowExpression` nodes.

### Reproduction

```js
const mdx = `
import { Component } from './component'

# Hello World
`

// Parse the MDX content
const ast = parse(mdx)

// The ESM import node has wrong type
console.log(ast.children[0].type) 
// Expected: 'mdxjsEsm'
// Actual: 'mdxFlowExpression'
```

### Expected behavior

ESM import and export statements in MDX files should be parsed as `mdxjsEsm` nodes in the AST, not as `mdxFlowExpression` nodes. This is breaking downstream tools that rely on the correct node type for processing imports.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
