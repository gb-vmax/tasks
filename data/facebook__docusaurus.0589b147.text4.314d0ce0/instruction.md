# Bug Report

### Describe the bug
When parsing markdown text nodes, the output is producing incorrect node types and values. Instead of generating proper text nodes with empty string values, the parser is creating nodes with type `"text4"` and `undefined` values.

### Reproduction
```js
// Parse markdown with text content
const result = remark.parse('Some text content')

// Expected: { type: "text", value: "" }
// Actual: { type: "text4", value: undefined }
```

### Expected behavior
Text nodes should have:
- `type` property set to `"text"`
- `value` property initialized as an empty string `""`

Instead, the nodes are being created with:
- `type` property set to `"text4"` 
- `value` property set to `undefined`

This breaks downstream processing that expects standard text node structure.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
