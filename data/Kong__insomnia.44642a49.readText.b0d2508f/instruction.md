# Bug Report

### Describe the bug

After a recent update, the plugin API's `clipboard.readText()` method is returning modified text instead of the raw clipboard content. The text appears to be sanitized in some way - null characters are being removed, line endings are being normalized, and multiple consecutive newlines are being collapsed.

### Reproduction

```js
// Plugin code
const clipboardText = context.app.clipboard.readText();

// Expected: Raw clipboard content exactly as copied
// Actual: Text with normalized line endings and removed null characters
```

For example:
1. Copy text with multiple blank lines (3+ newlines in a row)
2. Call `clipboard.readText()` from a plugin
3. The returned text only has 2 newlines max between content

Same issue with text containing null characters (`\0`) - they get stripped out completely.

### Expected behavior

`clipboard.readText()` should return the exact clipboard content without any modifications or sanitization. If sanitization is needed, it should be opt-in or done separately, not automatically applied to all clipboard reads.

### Additional context

This is breaking plugins that need to work with the raw clipboard data, especially when dealing with binary-like content or preserving exact formatting.

---
Repository: /testbed
