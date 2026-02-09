# Bug Report

### Describe the bug

I'm experiencing incorrect position tracking when parsing markdown with line endings. The parser seems to be calculating character offsets incorrectly, which causes issues when trying to map parsed tokens back to their original positions in the source text.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const source = `# Heading
Some text here
Another line`;

const result = await mdx.compile(source);

// When checking token positions, the offsets are wrong
// especially after line breaks (CRLF or LF)
```

The problem appears when processing documents with multiple lines. The character positions/offsets reported by the tokenizer don't match the actual positions in the source string.

### Expected behavior

Token positions should accurately reflect their location in the source document. This is important for:
- Source maps
- Error reporting
- Syntax highlighting
- Code transformations that need to preserve original positions

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
