# Bug Report

### Describe the bug

I'm experiencing an issue with the plugin data context where `getWorkspaces()` is not returning the expected results. After some recent changes, the function seems to be returning a Promise instead of the actual workspace data directly, which is breaking my plugin code.

### Reproduction

```js
// In a plugin context
const workspaces = data.getWorkspaces(projectId);

// This used to work but now fails
console.log(workspaces.length); // Error: Cannot read property 'length' of undefined
// or
// TypeError: workspaces.length is undefined

// The function now returns a Promise instead of the data directly
```

### Expected behavior

The `getWorkspaces()` function should return workspace data synchronously (or at least behave the same way it did before). My plugin code expects to be able to immediately access the returned workspaces without using async/await.

### Additional context

This seems to have broken after a recent update. The function signature appears to have changed but existing plugin code that relies on the synchronous behavior is now failing.

---
Repository: /testbed
