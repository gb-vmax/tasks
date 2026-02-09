# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it appears to be entering an infinite loop or hanging indefinitely when processing certain markdown content. The browser tab becomes unresponsive and eventually crashes.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test heading

Some paragraph text with **bold** content.

- List item 1
- List item 2
`;

// Parser hangs here and never completes
const result = remark.parse(markdown);
```

### Expected behavior

The parser should successfully parse the markdown content and return the AST without hanging or causing the process to become unresponsive.

### Additional context

This seems to have started happening recently. The same markdown content was parsing fine before. I've noticed it happens more frequently with content that has multiple formatting constructs (headings, lists, emphasis, etc.).

The issue is particularly problematic because it makes the entire application unresponsive - there's no timeout or error thrown, it just hangs indefinitely.

---
Repository: /testbed
