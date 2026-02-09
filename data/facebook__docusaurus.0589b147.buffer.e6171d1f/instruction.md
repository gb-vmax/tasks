# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with markdown parsing that seems to be related to fragment handling. When parsing certain markdown structures, the parser appears to be creating malformed AST nodes that cause downstream processing to fail.

### Reproduction

```js
import { remark } from 'remark';

const markdown = `
# Header

Some text with **bold** and *italic*.

- List item 1
- List item 2
`;

const processor = remark();
const result = processor.parse(markdown);

// Processing fails or produces unexpected output
console.log(result);
```

### Expected behavior

The markdown should parse correctly and produce a valid AST with properly structured fragment nodes containing children arrays.

### Additional context

This seems to affect any markdown content that triggers the internal buffer mechanism. The parser either crashes or produces malformed output that can't be properly serialized or transformed.

---
Repository: /testbed
