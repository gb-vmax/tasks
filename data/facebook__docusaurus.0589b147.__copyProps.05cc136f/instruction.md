# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties are being copied incorrectly. It seems like the logic for determining which properties to copy has been inverted.

### Reproduction

When using the bundled remark-gfm module, properties that should be excluded are being included, and properties that should be included are being excluded. This affects the behavior of the markdown processor.

```js
// Example scenario:
// When copying properties from one object to another with an exclusion list
// The excluded property is now being copied
// While all other properties are being ignored

const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
}

// If we try to copy all properties EXCEPT 'prop2'
// We end up with ONLY 'prop2' being copied
// Instead of prop1 and prop3
```

### Expected behavior

Properties should be copied correctly based on the exclusion logic. When a property is marked to be excluded, it should NOT be copied to the target object. All other properties should be copied normally.

### System Info
- Using the vendored remark-gfm@4.0.0 module
- This appears to affect the markdown parsing functionality

---
Repository: /testbed
