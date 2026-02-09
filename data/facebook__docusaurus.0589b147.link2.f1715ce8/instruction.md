# Bug Report

### Describe the bug
When parsing markdown links, the resulting node structure is malformed. The `type` field is being set to `null` instead of `"link"`, and the `children` array is also `null` instead of an empty array.

### Reproduction
```js
// Parse markdown with a link
const result = remark.parse('[example](https://example.com)');

// The link node has incorrect structure
console.log(result.children[0]);
// Expected: { type: "link", title: null, url: "https://example.com", children: [] }
// Actual: { type: null, title: null, url: "https://example.com", children: null }
```

### Expected behavior
Link nodes should have:
- `type` set to `"link"`
- `children` initialized as an empty array `[]`

Instead, both fields are being set to `null`, which breaks downstream processing that expects valid node types and array structures.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
