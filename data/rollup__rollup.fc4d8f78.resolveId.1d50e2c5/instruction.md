# Bug Report

### Describe the bug

I'm experiencing an issue with module resolution where the resolved ID information is being lost. When a plugin resolves a module ID to a string, the `resolvedBy` metadata that indicates which plugin performed the resolution is no longer being returned.

### Reproduction

```js
// Plugin that resolves IDs
const myPlugin = {
  name: 'my-resolver',
  resolveId(source) {
    if (source === 'special-module') {
      return 'path/to/special-module.js';
    }
  }
};

// When resolving 'special-module', the result no longer includes
// information about which plugin resolved it
```

### Expected behavior

When a plugin's `resolveId` hook returns a string, the resolution result should still include metadata about which plugin performed the resolution (the `resolvedBy` property). This is important for debugging and understanding the module resolution chain.

The returned object should be:
```js
{
  id: 'path/to/special-module.js',
  resolvedBy: 'my-resolver'
}
```

But instead it's just returning the string directly without the metadata.

### Additional context

This seems to affect the ability to track which plugins are resolving which modules, which makes debugging module resolution issues much harder. The `resolvedBy` information was previously available and was helpful for understanding the resolution process.

---
Repository: /testbed
