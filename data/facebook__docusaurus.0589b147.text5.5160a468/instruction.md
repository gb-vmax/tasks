# Bug Report

### Describe the bug

After a recent update, MDX text nodes are being generated with incorrect type and value properties. The text node type is being set to `"text5"` instead of `"text"`, and the value is `null` instead of an empty string `""`.

### Reproduction

```js
// When compiling MDX content, text nodes are created incorrectly
const result = compiler(options);
// Text nodes now have:
// { type: "text5", value: null }
// Instead of:
// { type: "text", value: "" }
```

This affects any MDX compilation that creates text nodes, causing downstream processing to fail or behave unexpectedly when it encounters the wrong node type or null values where strings are expected.

### Expected behavior

Text nodes should be created with:
- `type: "text"` (not `"text5"`)
- `value: ""` (empty string, not `null`)

This is breaking MDX parsing and rendering for our application.

---
Repository: /testbed
