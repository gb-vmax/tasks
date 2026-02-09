# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis markers in markdown output. When rendering emphasis nodes (italics), the opening marker appears to be missing from the generated output.

### Reproduction

```js
const tree = {
  type: 'emphasis',
  children: [
    { type: 'text', value: 'hello world' }
  ]
}

// Expected output: *hello world*
// Actual output: hello world*
```

When converting an emphasis node to markdown, only the closing marker is present in the output. The opening marker that should appear before the content is not included.

### Expected behavior

Both opening and closing emphasis markers should be present in the output. For example, `*text*` or `_text_` depending on the marker style being used.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
