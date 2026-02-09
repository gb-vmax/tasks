# Bug Report

### Describe the bug
When using the remark-gfm plugin to parse GitHub Flavored Markdown, the parsing fails and produces incorrect results. It seems like the markdown extensions are not being applied in the correct order or to the correct processing stages.

### Reproduction
```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkGfm from 'remark-gfm'

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)

const markdown = `
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
`

const result = processor.processSync(markdown)
// Expected: Properly parsed GFM table
// Actual: Table is not recognized or parsed incorrectly
```

### Expected behavior
The GFM extensions (tables, strikethrough, task lists, etc.) should be properly parsed and converted to the AST. The processor should correctly apply the micromark and fromMarkdown extensions.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems to have broken recently. The markdown processing pipeline doesn't seem to be working as expected anymore.

---
Repository: /testbed
