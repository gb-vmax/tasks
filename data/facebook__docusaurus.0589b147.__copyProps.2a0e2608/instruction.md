# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties are not being copied correctly. It seems like properties that should be excluded are being included, and properties that should be included are being excluded.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
}

const target = {}

// Try to copy all properties except 'prop2'
// Expected: target should have prop1 and prop3
// Actual: target only has prop2
```

When copying properties from one object to another with an exception parameter, the behavior is inverted - only the excepted property gets copied instead of all other properties.

### Expected behavior

When specifying a property to exclude during copying, all properties *except* that one should be copied to the target object. Currently it's doing the opposite.

### System Info
- rehype-stringify version: 10.0.0

---
Repository: /testbed
