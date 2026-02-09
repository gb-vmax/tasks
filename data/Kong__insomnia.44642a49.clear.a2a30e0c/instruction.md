# Bug Report

### Describe the bug
After a recent update, the clipboard functionality in plugins is behaving strangely. When I call `app.clipboard.clear()` from a plugin, it appears to be trying to read the clipboard contents first, which causes permission/access issues in certain environments.

### Reproduction
```js
// In a plugin context
module.exports.requestActions = [
  {
    label: 'Clear Clipboard',
    action: async (context) => {
      // This now fails with clipboard access errors
      context.app.clipboard.clear();
    }
  }
];
```

### Expected behavior
The `clear()` method should simply clear the clipboard without needing to read its current contents. Previously this worked fine, but now it's throwing errors about clipboard read permissions in some scenarios (particularly when the clipboard contains certain types of content or when running in restricted environments).

### Additional context
The error I'm seeing is related to clipboard read access, which shouldn't be necessary for a clear operation. It seems like the method is now doing more than just clearing the clipboard.

This is blocking my workflow as I have several plugins that rely on clearing the clipboard programmatically.

---
Repository: /testbed
