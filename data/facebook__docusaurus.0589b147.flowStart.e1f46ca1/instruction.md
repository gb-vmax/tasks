# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the parser seems to be entering duplicate states or causing unexpected behavior when processing flow content. The document structure appears malformed after parsing, and I'm seeing errors related to token management.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
# Heading

Some paragraph text here.

Another paragraph.
`

const result = remark().parse(markdown)
console.log(result)
```

When parsing markdown documents with multiple flow elements (paragraphs, headings, etc.), the output structure is incorrect. It looks like tokens are being duplicated or the flow state is not being managed properly during the parsing process.

### Expected behavior

The parser should correctly process flow content and produce a valid AST without duplicate or malformed token entries. Each chunk of flow content should be entered and exited exactly once.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
