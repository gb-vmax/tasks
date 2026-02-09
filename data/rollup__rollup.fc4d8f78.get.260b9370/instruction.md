# Bug Report

### Describe the bug

I'm experiencing an issue where accessing properties on the output bundle is returning the property key itself instead of the actual value. This seems to affect all property access on the bundle object.

### Reproduction

```js
const bundle = getOutputBundle({
  'index.js': {
    type: 'chunk',
    code: 'console.log("hello")'
  }
});

// Accessing a property returns the key instead of the value
console.log(bundle['index.js']); 
// Expected: { type: 'chunk', code: 'console.log("hello")' }
// Actual: 'index.js'
```

### Expected behavior

When accessing properties on the output bundle, it should return the actual property value (the chunk/asset object), not the property key string.

### Additional context

This breaks any code that tries to read from the output bundle. The proxy's `get` trap appears to be returning the key parameter directly instead of retrieving the value from the target object.

---
Repository: /testbed
