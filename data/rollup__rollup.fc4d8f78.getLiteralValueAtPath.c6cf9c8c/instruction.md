# Bug Report

### Describe the bug

I'm encountering unexpected behavior when accessing properties on objects. It seems like literal value resolution is returning incorrect values for certain property paths.

### Reproduction

```js
const obj = {
  foo: 'bar',
  nested: {
    value: 42
  }
}

// Accessing string-keyed properties
const result1 = obj.foo  // Expected: 'bar', but getting undefined behavior
const result2 = obj.nested.value  // Expected: 42, but not working as expected

// Non-integer property access seems broken
```

The issue appears when trying to access regular object properties. Instead of getting the actual values, I'm seeing undefined or unexpected results for string-based property keys.

### Expected behavior

When accessing object properties with string keys (non-integer paths), the literal values should be returned correctly. The current behavior seems to have the logic reversed - it's treating string properties as if they were numeric array indices.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be related to how object property paths are being evaluated internally. The behavior changed recently and is affecting property access patterns that worked before.

---
Repository: /testbed
