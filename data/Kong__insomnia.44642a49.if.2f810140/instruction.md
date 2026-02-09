# Bug Report

### Describe the bug

After a recent update, I'm getting unexpected behavior when exporting workspaces. The export function seems to hang or not return results properly. I think something changed with how workspaces are retrieved internally.

### Reproduction

```js
// In a plugin context
const workspaces = await data.export.workspaces();
console.log(workspaces); // This doesn't work as expected anymore
```

The issue appears when trying to export workspaces programmatically. The function used to return workspace data synchronously but now seems to expect async handling differently.

### Expected behavior

The workspace export should work the same way it did before - returning the list of workspaces without issues. Previously this worked fine but now the export functionality seems broken.

### Additional context

This might be related to how the internal `getWorkspaces` function is being called. I noticed the behavior changed after updating to the latest version. The export just doesn't complete properly anymore.

---
Repository: /testbed
