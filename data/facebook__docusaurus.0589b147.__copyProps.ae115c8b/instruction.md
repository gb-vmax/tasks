# Bug Report

### Describe the bug

I'm experiencing an issue with the `unist-util-remove-position` vendor module where object properties are not being copied correctly. It seems like the module is failing to copy properties from objects that aren't also functions.

### Reproduction

```js
const sourceObj = {
  prop1: 'value1',
  prop2: 'value2',
  nested: {
    data: 'test'
  }
};

const targetObj = {};

// Using the copyProps functionality
// Expected: all properties should be copied
// Actual: properties are not being copied
```

When trying to copy properties from a regular object (not a function), the properties don't get transferred to the target object. This breaks functionality that depends on property copying for plain objects.

### Expected behavior

The module should copy properties from both regular objects AND functions. Currently it seems to only work when the source is both an object AND a function simultaneously, which is essentially never true for normal objects.

### System Info
- Jest vendor module: unist-util-remove-position@5.0.0
- Affects property enumeration and copying behavior

---
Repository: /testbed
