# Bug Report

### Describe the bug

I'm experiencing an issue where object properties are being unexpectedly modified when they shouldn't be. It seems like the original object is being mutated instead of creating a new object with the merged properties.

### Reproduction

```js
const originalOptions = {
  setting1: 'value1',
  setting2: 'value2'
}

const defaultOptions = {
  setting2: 'default2',
  setting3: 'default3'
}

// After merging, originalOptions gets modified
const merged = map(originalOptions, defaultOptions)

// originalOptions now has setting3 added to it
// Expected: originalOptions should remain unchanged
console.log(originalOptions)
// Output: { setting1: 'value1', setting2: 'default2', setting3: 'default3' }
// Expected: { setting1: 'value1', setting2: 'value2' }
```

### Expected behavior

The `map` function should return a new merged object without modifying the original input objects. The original objects passed as arguments should remain unchanged after the merge operation.

### System Info
- Version: remark@15.0.1
- Node version: 18.x

---
Repository: /testbed
