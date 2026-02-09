# Bug Report

### Describe the bug

I'm encountering an issue with MDX paragraph rendering where paragraphs are not being generated correctly. The output seems malformed and breaks the document structure.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
This is a paragraph.

This is another paragraph.
`

const result = await compile(mdxContent)
```

When compiling MDX content with paragraphs, the resulting AST appears to have incorrect structure. Instead of getting proper paragraph nodes, the type and children properties seem wrong.

### Expected behavior

Paragraphs should be properly parsed and rendered with the correct node type and children array. The compiled output should preserve the paragraph structure from the MDX source.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
