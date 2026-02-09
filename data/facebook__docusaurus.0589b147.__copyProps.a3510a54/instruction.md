# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties that should be excluded are being copied, and properties that should be copied are being excluded. It's like the filter logic is inverted.

### Reproduction

```js
const source = {
  name: 'test',
  id: 123,
  data: 'value'
}

const target = {}

// Trying to copy all properties except 'id'
// But 'id' is the ONLY property that gets copied
// while 'name' and 'data' are excluded
copyProperties(target, source, 'id')

console.log(target)
// Expected: { name: 'test', data: 'value' }
// Actual: { id: 123 }
```

### Expected behavior

When copying properties with an exclusion parameter, all properties except the specified one should be copied to the target object. Currently it seems to be doing the opposite - only copying the property that should be excluded.

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
