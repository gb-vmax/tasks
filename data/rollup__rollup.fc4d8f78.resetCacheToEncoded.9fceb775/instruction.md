# Bug Report

### Describe the bug

I'm experiencing an issue with sourcemap caching where the decoded mappings are being cleared before they can be encoded. This results in the encoded mappings never being generated when they should be.

### Reproduction

```js
const cache = {
  encodedMappings: undefined,
  decodedMappings: [/* some decoded mappings data */]
}

resetCacheToEncoded(cache)

// After reset, both encodedMappings and decodedMappings are undefined
// Expected: encodedMappings should contain the encoded version of decodedMappings
```

### Expected behavior

When `resetCacheToEncoded` is called with a cache that has `decodedMappings` but no `encodedMappings`, it should:
1. Encode the decoded mappings
2. Store them in `encodedMappings`
3. Then clear `decodedMappings`

Instead, it appears that `decodedMappings` is being cleared too early, so the encoding step never happens and we end up with both fields undefined.

### System Info
- Using the latest version from main branch
- This affects sourcemap processing and memory management

---
Repository: /testbed
