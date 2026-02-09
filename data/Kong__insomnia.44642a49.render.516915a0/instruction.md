# Bug Report

### Describe the bug

I'm experiencing an issue with template rendering where dynamic values aren't being updated correctly. When I use `util.render()` in my templates with values that change between renders, the output shows stale/cached data instead of the current values.

### Reproduction

```js
// In a template extension
const context = {
  timestamp: Date.now()
};

// First render
const result1 = util.render('{{ timestamp }}'); // Returns e.g., 1234567890

// Wait a moment, timestamp changes
context.timestamp = Date.now();

// Second render
const result2 = util.render('{{ timestamp }}'); // Still returns 1234567890 instead of new value
```

The rendered output doesn't reflect the updated context values. It seems like the first result is being reused even when the underlying data has changed.

### Expected behavior

Each call to `util.render()` should evaluate the template with the current context values and return the updated result, not a cached version from a previous render.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with dynamic templates that rely on changing values like timestamps, random numbers, or iterative counters. Any help would be appreciated!

---
Repository: /testbed
