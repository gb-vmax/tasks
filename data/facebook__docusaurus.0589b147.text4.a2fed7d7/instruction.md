# Bug Report

### Describe the bug

I'm encountering an issue with text node generation in the markdown parser. When parsing markdown content that includes plain text, the resulting AST nodes have incorrect properties. Instead of getting a proper `text` type node with an empty string value, I'm seeing nodes with type `text4` and `null` values.

### Reproduction

```js
// Parsing simple markdown with text content
const result = remark.parse('Hello world');

// Expected: { type: 'text', value: 'Hello world' }
// Actual: { type: 'text4', value: null }
```

This affects any markdown content that contains text nodes, causing downstream processors to fail when they expect standard text node structures.

### Expected behavior

Text nodes in the AST should have:
- `type: "text"`
- `value: ""` (empty string as default)

Instead, they currently have:
- `type: "text4"` 
- `value: null`

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is breaking my markdown processing pipeline since other tools expect the standard `text` node type. Any help would be appreciated!

---
Repository: /testbed
