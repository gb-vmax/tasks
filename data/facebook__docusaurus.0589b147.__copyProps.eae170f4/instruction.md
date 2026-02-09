# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties are being copied incorrectly. It seems like the wrong properties are being transferred when using the copy utility.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  excluded: 'should not copy'
}

const target = {}

// Copy all properties except 'excluded'
copyProps(target, source, 'excluded')

// Expected: target should have prop1 and prop2, but not excluded
// Actual: target only has 'excluded' property
console.log(target)
// { excluded: 'should not copy' }
```

### Expected behavior

When copying properties with an exception parameter, all properties **except** the specified one should be copied to the target object. Instead, it appears that **only** the excluded property is being copied, which is the opposite of what should happen.

### Additional context

This is affecting property enumeration and object cloning operations. The behavior seems inverted - properties that should be excluded are included, and properties that should be included are excluded.

---
Repository: /testbed
