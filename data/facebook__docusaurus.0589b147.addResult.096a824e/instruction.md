# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs are being resolved incorrectly. It appears that the tokenizer is not properly handling event resolution, which causes some markdown elements to be skipped or processed in the wrong order.

### Reproduction

```js
const remark = require('remark');
const markdown = `
# Heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = remark().parse(markdown);
// Expected: All elements should be properly parsed
// Actual: Some elements are missing or in wrong positions
```

### Expected behavior

All markdown constructs should be resolved in the correct order and all events should be properly processed. The parser should not skip any elements during the tokenization phase.

### Additional context

This seems to affect nested or complex markdown structures more than simple ones. The issue appears to be related to how the resolver processes event slices during tokenization.

---
Repository: /testbed
