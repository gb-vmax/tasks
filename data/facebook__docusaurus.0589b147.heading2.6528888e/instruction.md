# Bug Report

### Describe the bug

I'm experiencing an issue with MDX heading parsing. When processing MDX documents with headings, the output structure appears to be malformed. Instead of getting proper heading nodes, I'm seeing nodes with an incorrect type and unexpected children.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some content here.
`

const result = await compile(mdxContent)
// The heading node has wrong type and contains undefined in children
```

When I parse MDX files containing headings (h1-h6), the resulting AST doesn't match what I expect. The heading nodes seem to have the wrong structure.

### Expected behavior

Headings should be parsed into proper heading nodes with:
- `type: "heading"`
- Correct `depth` value (1-6)
- Empty `children` array initially

Instead, I'm getting nodes with an unexpected type and children array containing undefined values.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken heading rendering in my documentation site. Any headings in MDX files are not displaying correctly.

---
Repository: /testbed
