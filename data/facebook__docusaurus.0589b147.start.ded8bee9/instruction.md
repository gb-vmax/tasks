# Bug Report

### Describe the bug

After a recent update, markdown parsing seems to be completely broken. When trying to parse markdown documents with link definitions, the parser throws an error or fails to process the content correctly.

### Reproduction

```js
const remark = require('remark');

const markdown = `
[example]: https://example.com "Example Site"

This is a [example] link.
`;

const result = remark().parse(markdown);
// Parser fails or produces unexpected output
```

### Expected behavior

The parser should correctly process markdown link definitions and return a valid AST. Link definitions like `[example]: https://example.com` should be parsed without errors.

### Additional context

This appears to affect any markdown document that contains link reference definitions. The issue started occurring after the latest changes to the tokenizer. Regular links without definitions seem to work fine, but documents with reference-style links fail to parse.

---
Repository: /testbed
