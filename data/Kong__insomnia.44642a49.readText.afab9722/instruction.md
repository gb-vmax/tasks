# Bug Report

### Describe the bug

After a recent update, the plugin API's `clipboard.readText()` method is returning empty strings or truncated content. The clipboard data seems to be getting sanitized/modified unexpectedly, which breaks plugins that rely on reading clipboard content.

### Reproduction

```js
// In a plugin context
app.clipboard.readText()
```

Expected: Returns the full clipboard text content
Actual: Returns empty string or truncated/modified text

### Steps to reproduce
1. Copy some text to the clipboard (e.g., a long JSON payload or text with special characters)
2. Call `app.clipboard.readText()` from a plugin
3. The returned value is empty, truncated, or has whitespace stripped

This is affecting plugins that need to read clipboard content for importing data or processing external content. The behavior changed recently and is breaking existing plugin functionality.

### Expected behavior
`clipboard.readText()` should return the exact clipboard content without modification, just like it did before.

### System Info
- Insomnia version: latest
- OS: Multiple (reproduced on macOS and Windows)

---
Repository: /testbed
