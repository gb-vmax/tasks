# Bug Report

### Describe the bug

I'm experiencing an issue with sourcemap caching where the decoded mappings are being cleared before they can be encoded. This seems to cause the encoded mappings to remain undefined when they should be populated.

### Reproduction

```js
// When resetCacheToEncoded is called with a cache that has:
// - encodedMappings: undefined
// - decodedMappings: [valid decoded data]

const cache = {
  encodedMappings: undefined,
  decodedMappings: someDecodedMappings
};

resetCacheToEncoded(cache);

// Expected: cache.encodedMappings should contain the encoded version
// Actual: cache.encodedMappings remains undefined
```

### Expected behavior

When resetting the cache to encoded format, if `encodedMappings` is undefined but `decodedMappings` exists, the decoded mappings should be encoded and stored before being cleared. The cache should end up with the encoded version available.

### Additional context

This appears to be affecting sourcemap processing where the decoded mappings get cleared too early in the reset process, preventing them from being properly encoded and cached.

---
Repository: /testbed
