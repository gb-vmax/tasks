# Bug Report

### Describe the bug

I'm experiencing an issue with spread operator behavior in nested object/array scenarios. When using the spread operator on objects that contain nested properties or arrays, the bundler isn't properly tracking mutations to deeply nested values.

### Reproduction

```js
const obj = {
  nested: {
    deep: {
      value: 1
    }
  }
};

const spread = { ...obj };

// Modifying deeply nested properties
spread.nested.deep.value = 2;

// The original object's nested properties are unexpectedly affected
console.log(obj.nested.deep.value); // Should be 1, but behavior is inconsistent
```

Similar issue with arrays:

```js
const arr = [[1, 2], [3, 4]];
const spreadArr = [...arr];

spreadArr[0][0] = 99;
// Original array is affected when it shouldn't be
```

### Expected behavior

The spread operator should properly handle nested object/array structures. Changes to properties that are more than one level deep in the spread copy should not affect the original object, and the bundler should correctly track these relationships for tree-shaking purposes.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to tree-shaking optimizations or how the spread operator is being analyzed.

---
Repository: /testbed
