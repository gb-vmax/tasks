# Bug Report

### Describe the bug
After a recent update, the clipboard functionality seems to be broken. When trying to copy text using the plugin API's `clipboard.writeText()`, nothing happens or the text doesn't get copied to the system clipboard correctly.

### Reproduction
```js
// Using the plugin context API
app.clipboard.writeText('Hello World');

// Expected: Text should be copied to clipboard
// Actual: Nothing gets copied or clipboard behavior is broken
```

I've also noticed that when trying to copy larger blocks of text or JSON data, the clipboard operation seems to fail silently.

### Expected behavior
The `clipboard.writeText()` method should copy the provided text to the system clipboard without any issues, regardless of the text content or length.

### System Info
- Insomnia version: latest
- OS: Various (reproduced on multiple systems)

This is blocking our workflow as we rely heavily on clipboard operations in our custom plugins. Any help would be appreciated!

---
Repository: /testbed
