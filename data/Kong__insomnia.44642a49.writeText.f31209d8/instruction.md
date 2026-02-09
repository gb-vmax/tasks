# Bug Report

### Describe the bug

After a recent update, the clipboard functionality in plugins appears to be broken. When trying to copy text using the app context API, nothing happens and the clipboard remains empty.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const { app } = context;
    
    // Try to copy some text
    app.clipboard.writeText('Hello World');
    
    // Clipboard is empty - nothing was copied
  }
];
```

Steps to reproduce:
1. Create a plugin that uses `app.clipboard.writeText()`
2. Try to copy any text to clipboard
3. Check clipboard contents - it's empty

### Expected behavior

The text should be copied to the clipboard successfully, just like it worked in previous versions.

### Additional context

This seems to have broken recently. The `readText()` method still works fine, but `writeText()` doesn't copy anything anymore. I'm using this in a custom plugin for copying API responses and it's currently not working at all.

---
Repository: /testbed
