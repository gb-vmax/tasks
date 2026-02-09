# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the parser seems to be crashing or producing incorrect AST nodes. The problem appears to be related to how node positions are being finalized during the parsing process.

### Reproduction

```js
import { parse } from 'remark-mdx'

const mdxContent = `
# Hello World

<Component prop="value" />

Some text here.
`

const ast = parse(mdxContent)
// Parser fails or produces malformed AST with incorrect position information
```

### Expected behavior

The parser should correctly parse MDX content and produce a valid AST with proper node positions and location data. All nodes should have accurate start/end positions that correspond to their actual location in the source text.

### Additional context

This seems to have started happening recently. The AST nodes are coming back with scrambled or undefined position information, which breaks downstream tools that rely on accurate source mapping.

---
Repository: /testbed
