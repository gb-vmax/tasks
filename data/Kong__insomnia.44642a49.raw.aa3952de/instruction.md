# Bug Report

### Describe the bug

The `data.import.raw()` plugin API method is not working correctly after a recent update. When trying to import data programmatically through a plugin, the function appears to be broken and doesn't complete the import process.

### Reproduction

```js
// In a plugin script
const result = await context.data.import.raw(jsonContent);
```

When calling this method, the import doesn't seem to work as expected. Previously this method would import the resources without any issues, but now it's not functioning properly.

### Expected behavior

The `data.import.raw()` method should successfully import the provided content into the active project, just like it did in previous versions. The import should complete without errors and the resources should be added to the project.

### Additional context

This appears to have broken recently - the method was working fine before. I'm using this in a custom plugin to import collections programmatically, and it's now preventing the plugin from functioning correctly.

---
Repository: /testbed
