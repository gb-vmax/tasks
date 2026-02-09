# Bug Report

### Describe the bug

The `app.getInfo()` plugin API is returning cached values that persist across multiple calls. When the app version or platform information changes (or in scenarios where fresh values are expected), the method returns stale data from a previous call instead of the current values.

### Reproduction

```js
// Plugin code
module.exports.requestHooks = [
  context => {
    const info1 = context.app.getInfo();
    console.log('First call:', info1);
    
    // Some time passes or app state changes
    
    const info2 = context.app.getInfo();
    console.log('Second call:', info2);
    
    // Both info1 and info2 reference the same object
    // Changes to the returned object affect future calls
  }
];
```

### Expected behavior

Each call to `getInfo()` should return a fresh object with the current version and platform information. The returned objects should be independent of each other.

### Actual behavior

The method returns the same cached object reference on every call. This means:
1. Multiple calls return the same object instance
2. If the returned object is modified, those modifications persist across calls
3. The version/platform values are only fetched once and then reused

### System Info
- Insomnia version: latest
- Platform: Cross-platform issue

---
Repository: /testbed
