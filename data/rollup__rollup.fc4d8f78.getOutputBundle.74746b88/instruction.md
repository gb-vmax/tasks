# Bug Report

### Describe the bug

I'm experiencing an issue with the output bundle proxy where deleting properties doesn't actually remove them from the bundle. When I try to delete a chunk or asset from the bundle, it appears to still be present afterwards.

### Reproduction

```js
const bundle = getOutputBundle(/* ... */);

// Add a chunk
bundle['chunk-abc.js'] = { /* chunk data */ };

// Try to delete it
delete bundle['chunk-abc.js'];

// The chunk is still there!
console.log(bundle['chunk-abc.js']); // Still returns the chunk instead of undefined
```

### Expected behavior

When using the `delete` operator on bundle properties, they should be removed from the bundle object. The property should return `undefined` after deletion.

### Additional context

This seems to affect the cleanup logic when managing output bundles. Not sure if this is related to the proxy implementation or something else, but it's causing issues with bundle manipulation in my build process.

---
Repository: /testbed
