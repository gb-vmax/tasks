# Bug Report

### Describe the bug

Getting an unexpected error when processing markdown content. The parser is throwing an error during normal operation, even when the input markdown is valid.

### Reproduction

```js
import { remark } from 'remark';
import remarkGfm from 'remark-gfm';

const markdown = `
# Hello

This is a test document with some **bold** text.
`;

const processor = remark().use(remarkGfm);
const result = processor.processSync(markdown);
// Error is thrown here
```

### Expected behavior

The markdown should be parsed successfully without throwing any errors. The processor should return the parsed AST or transformed content.

### Additional context

This seems to happen with any markdown input, even simple text. The error appears to be coming from somewhere in the remark-gfm plugin internals. Was working fine before, but now fails consistently.

---
Repository: /testbed
