# Bug Report

### Describe the bug

After a recent update, the plugin API seems to have broken. When trying to export data or interact with workspaces through the plugin context, I'm getting errors about `getWorkspaces` not being properly defined or returning unexpected results.

### Reproduction

```js
// In a plugin
module.exports.workspaceActions = [{
  label: 'Export Workspace',
  action: async (context, models) => {
    const workspaces = await context.data.export.insomnia({
      includePrivate: false,
      format: 'json'
    });
    console.log(workspaces);
  }
}];
```

When this action is triggered, it fails with an error related to workspace retrieval. The export functionality that was working before now seems to be broken.

### Expected behavior

The plugin should be able to export workspace data without errors, just like it did in previous versions.

### System Info
- Insomnia version: latest
- OS: macOS 14

This is blocking my workflow as I rely on this plugin for daily exports. Any help would be appreciated!

---
Repository: /testbed
