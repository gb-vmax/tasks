# Bug Report

### Describe the bug

After a recent update, paragraph nodes in MDX are not being generated correctly. The parser seems to be creating malformed paragraph objects that break the AST structure.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
This is a paragraph.

Another paragraph here.
`

const result = await compile(mdxContent)
```

When parsing MDX content with paragraphs, the resulting AST contains invalid paragraph nodes. The nodes have incorrect property names which causes downstream processing to fail.

### Expected behavior

Paragraph nodes should be created with the standard MDX AST structure:
- `type` should be `"paragraph"`
- `children` property should exist and be an array

Instead, the nodes appear to have different property names that don't match the expected schema.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
