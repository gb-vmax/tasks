# Bug Report

### Describe the bug

I'm experiencing issues with markdown parsing where line endings and buffer positions are being handled incorrectly. When parsing markdown content with specific line ending characters, the offset calculation seems off, and there are also problems with how the buffer index is being checked.

### Reproduction

```js
const remark = require('remark');

// Parse markdown with different line ending types
const markdown = `# Title\r\n\nSome content\r\nMore content`;

const result = remark.parse(markdown);

// Position information is incorrect for content after line endings
console.log(result.position);
```

When processing markdown that contains carriage return + line feed sequences (`\r\n`), the position tracking doesn't match the actual character positions in the source text. Additionally, there seem to be edge cases with buffer indexing that cause the parser to skip or misalign content.

### Expected behavior

The parser should correctly track positions for all types of line endings, and buffer index checks should properly handle boundary conditions to ensure accurate tokenization of the markdown content.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
