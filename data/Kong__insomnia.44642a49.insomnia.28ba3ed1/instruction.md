# Bug Report

### Describe the bug

The plugin export API is broken after a recent update. When trying to export workspace data using the `data.export.insomnia()` method, I'm getting syntax errors and the export functionality doesn't work at all.

### Reproduction

```js
const context = {
  data: {
    export: {
      insomnia: async (options) => {
        // Call the export function
        return await context.data.export.insomnia(options);
      }
    }
  }
};

// This throws an error
await context.data.export.insomnia({
  includePrivate: true,
  format: 'json'
});
```

### Expected behavior

The export should complete successfully and return the workspace data in the specified format. This was working fine before but now the entire export functionality seems to be broken.

### Additional context

It looks like there might be a syntax issue in the plugin context code. The export method doesn't seem to be properly defined anymore.

---
Repository: /testbed
