# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where attention markers (like `*` and `_` for emphasis) are not being recognized properly. When trying to parse markdown with emphasis or strong emphasis, the markers seem to be filtered out or not working as expected.

### Reproduction

```js
const markdown = '*italic text* and **bold text**';
const result = parseMarkdown(markdown);
// The emphasis markers are not being processed correctly
```

When I try to parse markdown containing asterisks or underscores for emphasis/strong emphasis, the output doesn't include the expected formatting nodes. It seems like the attention markers array is being modified in a way that prevents proper parsing.

### Expected behavior

The parser should correctly identify and process attention markers (`*`, `_`, etc.) to create emphasis and strong emphasis nodes in the AST. The markdown should be parsed with all emphasis formatting intact.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have started happening recently. The attention markers configuration appears to be getting filtered somehow which breaks the parsing of emphasized text.

---
Repository: /testbed
