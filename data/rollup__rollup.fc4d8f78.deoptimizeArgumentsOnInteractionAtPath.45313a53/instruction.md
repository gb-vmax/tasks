# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking when accessing properties on global objects. It seems like the bundler is incorrectly removing code that should be kept when dealing with nested property access on globals.

### Reproduction

```js
// This code gets incorrectly tree-shaken
const value = globalObject.property.nestedProperty;

// The bundler removes this even though it has side effects
globalObject.method.bind(this)();
```

When building with the latest version, code that accesses nested properties on global objects is being removed even when it shouldn't be. This appears to happen specifically when:

1. Accessing properties multiple levels deep on a global variable
2. Calling methods that are properties of global objects

The build output is missing these statements entirely, which breaks the application at runtime.

### Expected behavior

The bundler should preserve code that accesses nested properties on global objects, especially when those accesses could have side effects. The tree-shaking should correctly identify that these property accesses need to be retained.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
