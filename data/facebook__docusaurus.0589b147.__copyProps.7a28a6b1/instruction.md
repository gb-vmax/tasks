# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties that should be excluded are being copied, and properties that should be copied are being excluded. It seems like the logic is inverted.

### Reproduction

```js
const source = {
  name: 'test',
  id: 123,
  value: 'data'
}

const target = {}

// Trying to copy all properties except 'id'
// Expected: target should have 'name' and 'value', but not 'id'
// Actual: target only has 'id', missing 'name' and 'value'
```

When copying properties from one object to another with an exclusion parameter, the behavior is backwards - only the excluded property gets copied while all other properties are ignored.

### Expected behavior

When specifying a property to exclude during copying, that specific property should be skipped and all other properties should be copied to the target object.

### System Info
- Version: @mdx-js/mdx@3.0.0
- Node: 18.x

---
Repository: /testbed
