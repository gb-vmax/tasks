# Bug Report

### Describe the bug

The clipboard `clear()` method is throwing errors after a recent update. When I try to clear the clipboard in my plugin, it's failing with what looks like a syntax error or parsing issue.

### Reproduction

```js
// In my Insomnia plugin
module.exports.requestHooks = [
  context => {
    context.app.clipboard.writeText('some text');
    
    // This fails now
    context.app.clipboard.clear();
  }
];
```

### Expected behavior

The `clear()` method should successfully clear the clipboard without errors, just like it did before.

### System Info
- Insomnia version: Latest
- OS: Multiple platforms affected

The clipboard functionality was working fine previously, but something seems to have broken with the implementation. Any help would be appreciated!

---
Repository: /testbed
