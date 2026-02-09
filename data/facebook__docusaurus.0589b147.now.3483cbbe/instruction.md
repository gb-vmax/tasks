# Bug Report

### Describe the bug

I'm experiencing an issue with position tracking in the tokenizer. When parsing markdown content, the position information returned by the tokenizer appears to have swapped `offset` and `_index` values. This is causing incorrect position data to be reported.

### Reproduction

```js
// Parse some markdown content
const result = remark.parse('# Hello\n\nWorld');

// Check the position data returned by the tokenizer
// The offset and _index values appear to be swapped
console.log(result.position);
```

When inspecting the position objects during tokenization, the `offset` field contains what should be in `_index`, and vice versa.

### Expected behavior

The `offset` property should contain the actual offset value, and `_index` should contain the index value. These values should not be swapped in the returned position object.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to affect all position tracking throughout the parsing process. Any code relying on accurate position information will get incorrect values.

---
Repository: /testbed
