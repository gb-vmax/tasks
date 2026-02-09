# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with workspace retrieval in plugins. When calling the data context methods to get workspaces, the results seem to be cached and don't reflect recent changes. For example, if I create a new workspace or rename an existing one, the plugin still returns the old data.

### Reproduction

```js
// In a plugin
const workspaces1 = await context.data.export.workspaces();
console.log(workspaces1.length); // e.g., 5 workspaces

// Create a new workspace in the UI
// ...

// Immediately call again
const workspaces2 = await context.data.export.workspaces();
console.log(workspaces2.length); // Still shows 5 workspaces instead of 6
```

The same thing happens when:
1. Renaming a workspace - the old name is still returned
2. Deleting a workspace - it still appears in the list
3. Switching between projects - sometimes shows workspaces from the previous project

It seems like there's some caching happening that doesn't get invalidated when the underlying data changes. This wasn't happening in previous versions.

### Expected behavior

The workspace data should always reflect the current state. When I create, update, or delete workspaces, subsequent calls should return the updated information immediately.

### Additional context

This is affecting our plugin that relies on real-time workspace information. Users are seeing stale data which is causing confusion.

---
Repository: /testbed
