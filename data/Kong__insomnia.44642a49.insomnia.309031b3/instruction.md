# Bug Report

### Describe the bug

The `data.export.insomnia` plugin API is broken after a recent update. When trying to export workspace data, I'm getting syntax errors and the export functionality doesn't work at all.

### Reproduction

```js
const context = {
  data: {
    export: {
      insomnia: async (options) => {
        // This should export workspace data
        return await exportWorkspacesData(workspaces, includePrivate, format);
      }
    }
  }
};

// Trying to use the export function
await context.data.export.insomnia({
  workspace: myWorkspace,
  includePrivate: false,
  format: 'json'
});
```

### Expected behavior

The export function should successfully export workspace data in the specified format. It was working fine before but now it seems like the code structure got messed up somehow.

### System Info
- Insomnia version: latest
- OS: macOS

The export API appears to have some formatting issues in the source code. The function definition looks malformed and there seem to be helper functions defined in the wrong place.

---
Repository: /testbed
