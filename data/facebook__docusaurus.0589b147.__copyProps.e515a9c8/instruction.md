# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the rehype-stringify vendored module. It appears that properties are being incorrectly filtered when copying from one object to another. Properties that should be excluded are being included, and properties that should be included are being excluded.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  excludeMe: 'should not copy'
};

const target = {};

// Using the internal __copyProps with 'excludeMe' as the except parameter
// Expected: prop1 and prop2 should be copied, excludeMe should not
// Actual: Only excludeMe is copied, prop1 and prop2 are not
```

The issue seems to be in the property filtering logic - the condition for determining which properties to copy appears to be inverted. Additionally, the enumerable check logic also seems reversed.

### Expected behavior

When copying properties with an exclusion filter:
- All properties except the specified one should be copied to the target
- The enumerable attribute should be preserved correctly from the source property descriptor

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

This is affecting object property operations in the module and may cause unexpected behavior in property enumeration and copying scenarios.

---
Repository: /testbed
