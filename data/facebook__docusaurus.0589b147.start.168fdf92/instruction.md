# Bug Report

### Describe the bug

I'm encountering a critical issue where the markdown parser is completely broken. When trying to parse any markdown content with labels (like links or footnotes), the parser fails immediately.

### Reproduction

```js
const remark = require('remark');

const markdown = '[example](https://example.com)';
const result = remark().parse(markdown);
console.log(result);
```

This code throws an error because the `start` function in the label factory is missing. The parser can't handle any markdown that involves labels.

### Expected behavior

The markdown should parse successfully and return an AST with the link node properly structured.

### Additional context

This appears to affect all label-based markdown syntax including:
- Links: `[text](url)`
- Reference-style links: `[text][ref]`
- Footnotes (if using extensions)

The error occurs immediately when the parser tries to process the opening bracket `[` character. It seems like a critical function implementation is missing from the label factory.

---
Repository: /testbed
