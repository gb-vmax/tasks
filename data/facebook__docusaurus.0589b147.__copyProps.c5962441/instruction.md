# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties are being incorrectly excluded or included. When copying properties from one object to another, the behavior seems inverted - properties that should be copied are being skipped, and properties that should be excluded are being included.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
}

const target = {}

// Attempting to copy properties while excluding 'prop2'
// Expected: target should have prop1 and prop3
// Actual: target only has prop2 (the excluded property)
```

The property filtering logic appears to be inverted. When I specify a property to exclude, only that property gets copied instead of being excluded.

### Expected behavior

When copying properties with an exclusion parameter, all properties except the specified one should be copied to the target object. Currently it's doing the opposite.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
