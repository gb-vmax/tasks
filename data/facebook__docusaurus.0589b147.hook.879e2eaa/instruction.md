# Bug Report

### Describe the bug

The markdown parser appears to be breaking when processing certain constructs. After a recent update, the tokenizer seems to be incomplete and causes the parser to fail when trying to handle markdown syntax.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
# Test heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`

const result = remark().processSync(markdown)
console.log(result)
```

When running this code, the parser throws an error or produces incomplete/malformed output. It seems like the tokenizer is not properly handling the construct factory logic.

### Expected behavior

The markdown should be parsed correctly without errors, and all syntax elements (headings, bold, italic, lists) should be properly tokenized and processed.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This was working fine in previous versions, so it looks like something got broken in the tokenizer implementation. The issue seems to affect all markdown constructs, not just specific syntax elements.

---
Repository: /testbed
