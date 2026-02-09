# Bug Report

### Describe the bug

I'm experiencing a complete failure when trying to parse markdown content. The parser seems to break entirely and doesn't process any markdown syntax correctly. This appears to be affecting all markdown parsing operations.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
# Hello World

This is a **bold** text with *italic* words.

- List item 1
- List item 2
`

const result = remark().processSync(markdown)
console.log(result)
```

When running this code, the parser fails to process the markdown. It seems like the tokenization logic is broken and nothing gets parsed properly.

### Expected behavior

The markdown should be parsed correctly and converted to an AST/output format. All syntax elements (headings, bold, italic, lists) should be recognized and processed.

### Additional context

This seems to have started happening recently. The parser was working fine before but now it's completely broken. Looking at the code, it appears that some core tokenization functionality might be incomplete or corrupted.

The issue affects all markdown parsing operations, not just specific syntax elements. Even the simplest markdown documents fail to parse.

---
Repository: /testbed
