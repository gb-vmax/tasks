# Bug Report

### Describe the bug

After a recent update, I'm experiencing unexpected errors when processing markdown content. The parser is throwing "Validation failed" errors during normal operations, which seems to be coming from an internal validation function.

### Reproduction

```js
import {remark} from 'remark';

const processor = remark();
const markdown = `
# Hello World

This is a test document.
`;

// This throws an error now
const result = processor.processSync(markdown);
```

### Expected behavior

The markdown should be parsed successfully without throwing validation errors. This worked fine in previous versions and the markdown content is valid.

### Additional context

The error message is: `Error: Validation failed`

This seems to be affecting any markdown processing, not just specific edge cases. The validation is triggering even for simple, well-formed markdown documents.

---
Repository: /testbed
