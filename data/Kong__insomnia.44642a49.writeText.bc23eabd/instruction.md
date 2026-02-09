# Bug Report

### Describe the bug

After a recent update, the clipboard `writeText` function is not working as expected. When trying to copy text to clipboard, nothing happens and the text doesn't get copied. This seems to have broken existing functionality that was working fine before.

### Reproduction

```js
// This used to work but now fails silently
app.clipboard.writeText('some text');

// Also tried with different inputs
app.clipboard.writeText('test');
app.clipboard.writeText('hello world');
```

The clipboard remains empty after calling `writeText`. No errors are thrown, but the text is not being copied.

### Expected behavior

The text should be copied to the system clipboard when calling `writeText()`, just like it did in previous versions.

### Additional context

This is blocking our workflow as we rely on programmatic clipboard operations in our plugin. The function signature appears to be the same, but the behavior has changed.

---
Repository: /testbed
