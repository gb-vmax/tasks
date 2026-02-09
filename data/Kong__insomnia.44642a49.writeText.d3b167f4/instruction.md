# Bug Report

### Describe the bug

After a recent update, the clipboard functionality seems to be modifying text in unexpected ways. When copying text that contains multiple spaces or line breaks, the content gets altered before being written to the clipboard.

### Reproduction

```js
// Copy text with multiple spaces
app.clipboard.writeText('Hello    World');
// Expected: 'Hello    World'
// Actual: 'Hello World' (spaces collapsed to single space)

// Copy text with multiple newlines
app.clipboard.writeText('Line1\n\n\nLine2');
// Expected: 'Line1\n\n\nLine2'
// Actual: 'Line1\n\nLine2' (newlines collapsed)
```

### Expected behavior

The clipboard should preserve the exact text that's passed to `writeText()`, including multiple consecutive spaces and newlines. Users may intentionally want to copy formatted text with specific whitespace.

### Additional context

This is particularly problematic when copying code snippets or formatted data where whitespace is significant. The text sanitization appears to be happening automatically but wasn't documented in the changelog.

---
Repository: /testbed
