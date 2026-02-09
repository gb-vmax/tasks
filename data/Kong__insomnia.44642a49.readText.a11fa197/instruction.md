# Bug Report

### Describe the bug

After a recent update, the plugin API's `app.clipboard.readText()` method is now modifying the clipboard content that it returns. Special characters and whitespace formatting are being stripped or altered, which breaks workflows that depend on reading exact clipboard content.

### Reproduction

```js
// In a plugin
const clipboardContent = await app.clipboard.readText();

// If clipboard contains:
// "Line 1\r\nLine 2\r\n\r\n\r\nLine 3  "

// Expected: "Line 1\r\nLine 2\r\n\r\n\r\nLine 3  "
// Actual: "Line 1\nLine 2\n\nLine 3"
```

The method is now:
1. Removing carriage returns (`\r`)
2. Stripping trailing spaces from lines
3. Collapsing multiple newlines
4. Removing control characters

### Expected behavior

`readText()` should return the exact clipboard content without any modifications or sanitization. Plugins should receive the raw text and decide themselves if they want to process it.

This is breaking plugins that need to:
- Preserve exact formatting (e.g., Windows-style line endings)
- Work with control characters
- Maintain trailing whitespace
- Handle multiple consecutive newlines

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
