# Bug Report

### Describe the bug

I'm encountering unexpected behavior when accessing properties on object prototypes. It seems like the literal value resolution has changed and is now returning incorrect values for certain property paths.

### Reproduction

```js
const obj = Object.create({});

// Accessing a string property on the prototype
const value = obj.someProperty;

// Expected: undefined (or the actual property value if it exists)
// Actual: Returns UnknownValue in some cases where it should return undefined
```

The issue appears when trying to get literal values at specific paths on objects. Properties that should resolve to `undefined` are instead being treated as unknown values, which affects how the code is processed.

### Expected behavior

When accessing properties on object prototypes:
- String-keyed properties should return `undefined` when they don't exist
- The behavior should be consistent with how JavaScript normally handles prototype property access
- Number properties (like array indices) should continue to work as expected

### Additional context

This seems to affect how object property access is analyzed. The logic for determining when to return `undefined` vs `UnknownValue` appears to have been inverted or changed in a way that breaks the expected behavior.

---
Repository: /testbed
