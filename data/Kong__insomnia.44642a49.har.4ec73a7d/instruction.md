# Bug Report

### Describe the bug

The plugin data context `har` export function is not working correctly. When trying to export HAR data, I'm getting a syntax error that prevents the export from completing.

### Reproduction

```js
const context = init(projectId);

// This fails with a syntax error
const harData = await context.data.export.har({
  workspace: myWorkspace,
  includePrivate: true
});
```

### Expected behavior

The HAR export should complete successfully and return the HAR data without any syntax errors. The function worked fine before but now seems to have an issue with its structure.

### Additional context

This appears to be affecting all HAR exports through the plugin context, regardless of the options passed. The error occurs immediately when trying to call the function.

---
Repository: /testbed
