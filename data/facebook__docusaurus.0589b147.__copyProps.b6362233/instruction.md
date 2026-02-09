# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties that should be excluded are being copied, and properties that should be copied are being excluded instead. It appears the logic for filtering properties during the copy operation is inverted.

### Reproduction

```js
const source = {
  name: 'test',
  value: 123,
  internal: 'should-be-excluded'
};

const target = {};

// Attempting to copy all properties except 'internal'
// But 'internal' gets copied and everything else is excluded
copyProperties(target, source, 'internal');

console.log(target);
// Expected: { name: 'test', value: 123 }
// Actual: { internal: 'should-be-excluded' }
```

### Expected behavior

When copying properties from one object to another with an exception parameter, all properties except the specified one should be copied to the target object. Currently it's doing the opposite - only copying the property that should be excluded.

### System Info

- Version: remark-rehype@11.0.0
- Node: v18.x

---
Repository: /testbed
