# Bug Report

### Describe the bug

After a recent update, the markdown parser is completely broken. When trying to parse any markdown content, the parser fails to process the text correctly and returns incomplete or malformed output.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
# Hello World

This is a test paragraph.

- Item 1
- Item 2
`

const result = remark().processSync(markdown)
console.log(result)
```

### Expected behavior

The parser should correctly tokenize and process the markdown content, returning a proper AST. Instead, it seems like the tokenizer is not completing its work and the parsing process is interrupted prematurely.

### Additional context

This affects all markdown parsing operations. Even simple text without any special markdown syntax fails to parse correctly. The issue appears to be related to the tokenization phase of the parser.

---
Repository: /testbed
