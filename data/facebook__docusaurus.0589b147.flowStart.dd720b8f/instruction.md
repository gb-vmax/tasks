# Bug Report

### Describe the bug
When parsing markdown documents that end without a trailing newline, the parser seems to hang or produce incorrect output. The issue appears to be related to how the document flow handles EOF (end-of-file) conditions.

### Reproduction
```js
import {remark} from 'remark'

const markdown = `# Hello

This is a test` // Note: no trailing newline

const result = remark().parse(markdown)
console.log(result)
```

The parser either doesn't complete properly or produces malformed AST output when the document ends abruptly without a newline character.

### Expected behavior
The parser should handle documents without trailing newlines gracefully and produce the correct AST structure, just as it does for documents with proper line endings.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
