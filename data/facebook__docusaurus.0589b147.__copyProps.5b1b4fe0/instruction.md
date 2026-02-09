# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the mdast-util-to-string vendor module. When using the `__copyProps` utility function, properties that should be excluded are actually being copied, while all other properties are being skipped. This is the opposite of what should happen.

### Reproduction

```js
const source = {
  foo: 'value1',
  bar: 'value2',
  baz: 'value3'
};

const target = {};

// Trying to copy all properties EXCEPT 'bar'
__copyProps(target, source, 'bar');

// Expected: target should have 'foo' and 'baz'
// Actual: target only has 'bar'
console.log(target); // { bar: 'value2' }
```

The function is copying only the property that was meant to be excluded, and excluding all the properties that should have been copied.

### Expected behavior

When calling `__copyProps(target, source, 'bar')`, the function should copy all properties from `source` to `target` **except** for the property named `'bar'`. Instead, it's doing the reverse - only copying `'bar'` and excluding everything else.

### System Info

- Jest vendor module: mdast-util-to-string@4.0.0
- Affected function: `__copyProps`

---
Repository: /testbed
