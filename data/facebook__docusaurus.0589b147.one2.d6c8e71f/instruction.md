# Bug Report

### Describe the bug

The `zwitch` function is crashing when trying to process values that don't have the expected key property. Getting a `TypeError: Cannot read property of undefined` error when the value object is missing the key being switched on.

### Reproduction

```js
const handler = zwitch('type', {
  handlers: {
    foo: (node) => 'handled foo',
    bar: (node) => 'handled bar'
  },
  unknown: (node) => 'unknown type'
})

// This crashes instead of calling the unknown handler
const result = handler({}) // value without 'type' property
```

### Expected behavior

When a value doesn't have the key property, it should fall back to the `unknown` handler instead of throwing an error. The function used to check if the key exists on the value before trying to access it.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
