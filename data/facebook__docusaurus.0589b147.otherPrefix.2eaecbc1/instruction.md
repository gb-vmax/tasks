# Bug Report

### Describe the bug

I'm encountering an issue with markdown list parsing where list items without proper whitespace after the marker are being incorrectly accepted. The parser seems to be allowing malformed list syntax that should be rejected.

### Reproduction

```js
const markdown = `
1.item without space
- another item without space
`;

// These should fail to parse as valid list items
// but are currently being accepted
```

When parsing markdown lists, the spec requires whitespace between the list marker (like `1.` or `-`) and the item content. However, the parser is currently accepting list items even when this required whitespace is missing.

### Expected behavior

List items without whitespace after the marker should not be parsed as valid lists. The parser should reject malformed syntax like:
- `1.item` (should be `1. item`)
- `-item` (should be `- item`)

Only properly formatted list items with the required whitespace should be accepted.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
