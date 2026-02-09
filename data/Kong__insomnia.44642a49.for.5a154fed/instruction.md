# Bug Report

### Describe the bug
When using `combinedMapKeys()` utility function, the returned array doesn't contain all the unique keys from the input maps. It appears that some keys are being skipped or not properly collected.

### Reproduction
```js
const map1 = { key1: 'value1', key2: 'value2' };
const map2 = { key3: 'value3', key4: 'value4' };

const result = combinedMapKeys([map1, map2]);

// Expected: ['key1', 'key2', 'key3', 'key4']
// Actual: Missing keys or incorrect output
console.log(result);
```

### Expected behavior
The function should return an array containing all unique keys from all the input maps. For example, if you pass two maps with keys `key1`, `key2` and `key3`, `key4` respectively, it should return `['key1', 'key2', 'key3', 'key4']`.

### Additional context
This is affecting VCS sync operations where we need to combine snapshot state maps and status candidate maps. The missing keys are causing some files/resources to not be properly tracked during sync.

---
Repository: /testbed
