# Bug Report

### Describe the bug

I'm experiencing an issue where object properties are being set incorrectly when using the `mark` function. Instead of the property being set to the intended value, it's being set to the key name itself.

### Reproduction

```js
const values = {};
const key = 'myProperty';
const value = 'expectedValue';

mark(values, key, value);

console.log(values.myProperty); // Outputs: 'myProperty' instead of 'expectedValue'
```

### Expected behavior

The `values` object should have the property set to the actual value passed in, not the key name. In the example above, `values.myProperty` should equal `'expectedValue'`, not `'myProperty'`.

This seems to have started happening recently and is causing data to be stored incorrectly throughout the application.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
