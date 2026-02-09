# Bug Report

### Describe the bug

The plugin API's `clipboard.readText()` method is returning sanitized/modified content instead of the raw clipboard text. This breaks plugins that need to work with the actual clipboard contents, especially when dealing with code snippets or structured data that might contain patterns that look like HTML/JavaScript.

### Reproduction

```js
// In a plugin context
const clipboardContent = context.app.clipboard.readText();

// If clipboard contains: "<script>console.log('test')</script>"
// Expected: "<script>console.log('test')</script>"
// Actual: "" (empty string - content was stripped)

// If clipboard contains: "onclick='handleClick()'"
// Expected: "onclick='handleClick()'"
// Actual: "" (event handler attribute removed)
```

### Expected behavior

`clipboard.readText()` should return the exact clipboard content without any modifications or sanitization. Plugins should be able to handle the raw data themselves if they need to sanitize it.

### Additional context

This seems to have started happening recently. The method is now stripping out:
- Script tags
- Event handler attributes (onclick, onload, etc.)
- javascript: protocol strings

This makes it impossible to use the clipboard API for legitimate use cases like:
- Copying/pasting code snippets that contain these patterns
- Working with HTML templates
- Handling event handler code in development tools

---
Repository: /testbed
