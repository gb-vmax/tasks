# Bug Report

### Describe the bug

I'm encountering an issue with the VCS sync functionality where some keys are being dropped when combining maps. It seems like not all keys from the input maps are being included in the combined result.

### Reproduction

```js
const map1 = { key1: 'value1', key2: 'value2', key3: 'value3' };
const map2 = { key4: 'value4', key5: 'value5' };

const combined = combinedMapKeys([map1, map2]);

// Expected: ['key1', 'key2', 'key3', 'key4', 'key5']
// Actual: Missing the first key from each map
console.log(combined);
```

### Expected behavior

All keys from all input maps should be present in the combined output. Currently it looks like the first key from each map is being skipped, which breaks the sync state tracking.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
