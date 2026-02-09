# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties are being copied incorrectly. It seems like properties that should be excluded are being included, and properties that should be included are being excluded instead.

### Reproduction

```js
const source = {
  name: 'test',
  value: 42,
  internal: 'should be excluded'
}

const target = {}

// Copy all properties except 'internal'
copyProperties(target, source, 'internal')

// Expected: target should have 'name' and 'value' but not 'internal'
// Actual: target only has 'internal' and is missing 'name' and 'value'
console.log(target)
// Output: { internal: 'should be excluded' }
// Expected: { name: 'test', value: 42 }
```

### Expected behavior

When copying properties from one object to another with an exclusion parameter, all properties except the specified one should be copied to the target object. The excluded property should not appear in the target.

### System Info
- Version: remark@15.0.1
- Node: 18.x

---
Repository: /testbed
