# Bug Report

### Describe the bug

I'm encountering an issue with sourcemap caching where the encoded mappings are being unexpectedly cleared. After calling the cache reset function, both the decoded AND encoded mappings become undefined, which causes problems when trying to access the sourcemap data later.

### Reproduction

```js
const cache = {
  encodedMappings: "AAAA,CAAC,CAAC",
  decodedMappings: undefined
};

// Reset the cache
resetCacheToEncoded(cache);

// Expected: cache.encodedMappings should still be "AAAA,CAAC,CAAC"
// Actual: cache.encodedMappings is now undefined
console.log(cache.encodedMappings); // undefined (should be the original string)
```

### Expected behavior

When resetting the cache to encoded format, the function should:
1. Keep the existing encoded mappings if they already exist
2. Only clear the decoded mappings to free up memory
3. NOT clear the encoded mappings since that's what we're resetting TO

The whole point of this function seems to be optimizing memory by keeping only the encoded version, but it's clearing both which defeats the purpose.

### System Info
- Version: latest from main branch

This is causing issues in production where sourcemaps become unavailable after the cache reset is triggered.

---
Repository: /testbed
