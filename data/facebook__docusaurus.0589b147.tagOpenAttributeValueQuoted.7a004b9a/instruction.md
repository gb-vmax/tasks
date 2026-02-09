# Bug Report

### Describe the bug

HTML tags with quoted attribute values are not being parsed correctly. When processing markdown that contains HTML tags with attributes like `<div class="test">`, the parser appears to reject valid HTML instead of accepting it.

### Reproduction

```js
const markdown = '<div class="example">Content</div>';
// Parser fails to recognize this as valid HTML
```

Try parsing any HTML tag with quoted attributes in markdown:
- `<span id="myid">text</span>`
- `<a href="https://example.com">link</a>`
- `<img src="image.jpg" alt="description">`

All of these should be valid HTML in markdown but are being rejected.

### Expected behavior

HTML tags with quoted attribute values should be parsed and recognized as valid HTML elements. The markdown processor should accept standard HTML syntax including attributes with quoted values.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
