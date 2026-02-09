# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties that already exist on the target object are being overwritten when they shouldn't be. This appears to be happening in the property copying utility function.

### Reproduction

```js
const target = {
  existingProp: 'original value',
  anotherProp: 'should stay'
}

const source = {
  existingProp: 'new value',
  newProp: 'added'
}

// After copying properties from source to target
// existingProp gets overwritten to 'new value'
// but it should remain 'original value'
```

### Expected behavior

When copying properties between objects, existing properties on the target should be preserved and not overwritten. Only properties that don't already exist on the target should be copied from the source.

### System Info
- Version: latest
- Node: v18.x

---
Repository: /testbed
