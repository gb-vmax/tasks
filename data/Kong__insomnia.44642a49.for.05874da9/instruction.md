# Bug Report

### Describe the bug

I'm experiencing an issue with the VCS utility function that combines map keys. When I have multiple maps with different keys, the function is not returning all the unique keys as expected. Instead, it seems to be returning an incomplete or incorrect set of keys.

### Reproduction

```js
const map1 = { key1: 'value1', key2: 'value2', key3: 'value3' };
const map2 = { key4: 'value4', key5: 'value5' };
const map3 = { key6: 'value6', key7: 'value7' };

const result = combinedMapKeys([map1, map2, map3]);
// Expected: ['key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7']
// Actual: Only getting the first key from each map or missing keys
```

This is breaking my sync functionality where I need to get all unique keys across multiple snapshot state maps. The function used to work correctly but now it's not collecting all the keys properly.

### Expected behavior

The `combinedMapKeys` function should return an array containing all unique keys from all the input maps. Every key that appears in any of the maps should be included in the result.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
