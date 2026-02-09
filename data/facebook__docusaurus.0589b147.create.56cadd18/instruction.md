# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where the tokenizer initialization seems to be broken. When trying to parse markdown content, the parser appears to be receiving incorrect arguments or parameters in the wrong order, causing parsing to fail or behave unexpectedly.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Hello World

This is a test document.
`;

const result = remark.parse(markdown);
// Parser fails or produces incorrect output
```

### Expected behavior

The markdown should be parsed correctly and return a proper AST structure. The tokenizer should receive the correct parameters in the right order during initialization.

### Additional context

This seems to have started happening recently. The parser was working fine before but now it's not processing markdown content as expected. It looks like there might be an issue with how the tokenizer creator function is handling its parameters.

---
Repository: /testbed
