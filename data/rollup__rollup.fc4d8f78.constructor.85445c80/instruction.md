# Bug Report

### Describe the bug

I'm experiencing an issue where object member access seems to be completely broken. When trying to access properties on objects, the behavior is completely wrong - it appears that the object and property path are getting mixed up somehow.

### Reproduction

```js
const obj = {
  foo: {
    bar: 'value'
  }
}

// Trying to access obj.foo.bar
const result = obj.foo.bar
// Expected: 'value'
// Actual: undefined or incorrect value
```

This also affects more complex scenarios:

```js
const config = {
  settings: {
    enabled: true,
    timeout: 5000
  }
}

// Accessing nested properties returns wrong values
console.log(config.settings.enabled) // Should be true, but getting unexpected results
```

### Expected behavior

Object property access should work correctly and return the expected values from the object structure. Nested property access should traverse the object hierarchy properly.

### Additional context

This seems to affect all object member access patterns. The issue appears to be internal to how object members are being resolved - like the object reference and the property path are being swapped or confused somehow.

---
Repository: /testbed
