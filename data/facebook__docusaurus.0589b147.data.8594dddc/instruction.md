# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the parser seems to be entering an infinite loop or hanging indefinitely when processing certain text content. The application becomes unresponsive and never completes the parsing operation.

### Reproduction

```js
const remark = require('remark');

const markdown = `
This is some text with line breaks.

Another paragraph here.
`;

// Parser hangs and never completes
const result = remark.parse(markdown);
```

### Expected behavior

The markdown should be parsed successfully and return the AST without hanging. The parser should handle line breaks and paragraph boundaries correctly.

### Additional context

This seems to have started happening recently. The parser gets stuck when processing data tokens and doesn't properly exit or transition states. It appears to be related to how the parser handles break conditions in text content.

---
Repository: /testbed
