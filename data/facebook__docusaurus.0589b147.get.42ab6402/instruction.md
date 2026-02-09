# Bug Report

### Describe the bug

I've encountered an issue with property copying in the vendored `estree-util-value-to-estree` module. When copying properties from one object to another, the getter function is returning the wrong value - it's using the property descriptor object as a key instead of the actual property key.

### Reproduction

```js
const source = {
  foo: 'bar',
  baz: 'qux'
};

const target = {};

// When __copyProps is called internally
// The getter should return from[key] but instead returns from[desc]
// where desc is the property descriptor object
```

This results in accessing properties on the copied object returning `undefined` or incorrect values since `from[desc]` doesn't make sense (desc is an object, not a string key).

### Expected behavior

When properties are copied, the getter should access the source object using the property key, not the descriptor object. The copied properties should return the same values as the original object.

### System Info
- Affected file: `jest/vendor/estree-util-value-to-estree@3.0.1.js`
- Line 13 in the `__copyProps` helper function

---
Repository: /testbed
