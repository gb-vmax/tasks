# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with markdown parsing. The parser seems to hang or fail to process content correctly, particularly when dealing with complex nested structures or certain token patterns.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
# Test Document

Some text with **bold** and *italic*.

- List item 1
- List item 2

> Blockquote
`;

const result = remark().processSync(markdown);
// Parser fails or produces incomplete output
```

### Expected behavior

The markdown should be parsed completely and all tokens should be processed correctly. Previously this worked fine, but now the parser seems to stop processing partway through or produces malformed output.

### Additional context

This appears to affect various markdown constructs including lists, blockquotes, and inline formatting. The issue manifests inconsistently but is reproducible with documents containing multiple nested elements.

---
Repository: /testbed
