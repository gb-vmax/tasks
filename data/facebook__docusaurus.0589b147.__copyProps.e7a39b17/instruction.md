# Bug Report

### Describe the bug
When using the remark-directive plugin, object properties are not being copied correctly. Properties that should be excluded are being included, and properties that should be included are being excluded.

### Reproduction
```js
const remarkDirective = require('remark-directive');

// Create an object with multiple properties
const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
};

// Try to copy properties while excluding 'prop2'
const target = {};
// Use the internal __copyProps logic
// Expected: target should have prop1 and prop3, but NOT prop2
// Actual: target only has prop2, missing prop1 and prop3
```

### Expected behavior
When copying object properties with an exclusion list, all properties except the excluded ones should be copied to the target object. Currently, the behavior is inverted - only the excluded property is being copied while all others are ignored.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
