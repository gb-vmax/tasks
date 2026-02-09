# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in GFM (GitHub Flavored Markdown) parsing. When parsing markdown content that contains footnote calls, the parser seems to get stuck or produce incorrect AST structure.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkGfm = require('remark-gfm')

const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
`

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)

const ast = processor.parse(markdown)
const result = processor.runSync(ast)

// Parser hangs or produces malformed AST
console.log(result)
```

### Expected behavior

The markdown should parse correctly and produce a valid AST with proper footnote reference and definition nodes. The parser should complete without hanging.

### Additional context

This seems to affect any markdown document containing footnote syntax (`[^1]`). The issue appears to be related to how footnote calls are being processed during the exit phase of parsing.

---
Repository: /testbed
