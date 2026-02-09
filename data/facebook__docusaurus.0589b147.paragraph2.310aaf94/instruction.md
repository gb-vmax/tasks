# Bug Report

### Describe the bug

I'm encountering an issue with paragraph nodes in MDX compilation. When processing MDX content, paragraph elements are being generated with incorrect structure - the `type` field is an array instead of a string, and `children` is set to `null` instead of an empty array.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
This is a simple paragraph.

Another paragraph here.
`

const result = await compile(mdxContent)
```

When the compiler processes this content, the paragraph nodes have malformed structure:
- `type` is `["paragraph"]` instead of `"paragraph"`
- `children` is `null` instead of `[]`

This causes downstream processing to fail since the AST structure is invalid.

### Expected behavior

Paragraph nodes should have:
- `type` as a string: `"paragraph"`
- `children` as an array: `[]`

This matches the structure of other node types in the AST and is required for proper MDX processing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
