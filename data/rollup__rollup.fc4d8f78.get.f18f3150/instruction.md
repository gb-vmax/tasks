# Bug Report

### Describe the bug

I'm experiencing an issue with the output bundle where accessing properties returns incorrect values. It seems like the proxy is returning the wrong data - instead of getting the actual property values from the bundle, I'm getting what appears to be a set of lowercase keys regardless of which property I'm trying to access.

### Reproduction

```js
const bundle = getOutputBundle({
  'main.js': {
    type: 'chunk',
    code: '...'
  }
});

// Trying to access the chunk
console.log(bundle['main.js']); 
// Expected: { type: 'chunk', code: '...' }
// Actual: Set of lowercase bundle keys
```

### Expected behavior

When accessing properties on the output bundle, it should return the actual chunk/asset data, not the internal set of reserved lowercase keys.

### Additional context

This appears to affect all property access on the output bundle proxy. Any property I try to access returns the same set object instead of the expected value.

---
Repository: /testbed
