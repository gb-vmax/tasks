# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM imports where the AST node type is incorrect. When parsing MDX files with ESM import/export statements, the generated node type is `mdxFlowEsm` instead of the expected `mdxjsEsm`.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
import { Component } from './component'

# Hello World
`

const result = await compile(mdxContent)
// The AST contains nodes with type "mdxFlowEsm" instead of "mdxjsEsm"
```

When inspecting the generated AST, ESM import/export nodes have the wrong type identifier, which breaks any tooling or plugins that expect the standard `mdxjsEsm` node type.

### Expected behavior

ESM import/export statements should generate AST nodes with type `mdxjsEsm` to maintain consistency with the MDX specification and existing tooling.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
