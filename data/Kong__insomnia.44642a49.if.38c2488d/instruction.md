# Bug Report

### Describe the bug

After a recent update, the `database.remove()` function appears to be broken. When trying to remove documents from the database, I'm getting errors or the function doesn't execute at all.

### Reproduction

```js
const doc = await database.get('Request', 'req_123');
await database.remove(doc);
```

When running this code, the removal fails. It looks like there might be an issue with how the function is structured - the code doesn't seem to execute properly.

### Expected behavior

The document and its descendants should be removed from the database without errors. The function should handle the removal operation cleanly like it did before.

### Additional context

This was working fine in the previous version. I noticed the issue started appearing after the latest changes to the database module. The function signature seems to have changed but the implementation looks off - there's duplicate code or something that's preventing it from running correctly.

---
Repository: /testbed
