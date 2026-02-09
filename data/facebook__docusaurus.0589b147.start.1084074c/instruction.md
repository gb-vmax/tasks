# Bug Report

### Describe the bug

After a recent update, markdown definition parsing appears to be broken. When trying to parse markdown documents that contain reference-style links with definitions, the parser crashes or produces unexpected results.

### Reproduction

```js
const remark = require('remark');

const markdown = `
[link]: https://example.com "Example"

This is a [link] to somewhere.
`;

const result = remark().parse(markdown);
// Parser fails to process the definition correctly
```

### Expected behavior

The parser should correctly handle markdown definitions (reference-style links) and parse them into the appropriate AST nodes without errors. The definition should be recognized and the link reference should work properly.

### Additional context

This seems to have started happening recently. The issue occurs specifically when parsing documents with link definitions in the format `[identifier]: url "title"`. Regular inline links still work fine, but reference-style links are not being processed correctly.

---
Repository: /testbed
