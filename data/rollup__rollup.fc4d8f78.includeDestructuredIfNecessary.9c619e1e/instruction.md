# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignments where properties are not being included correctly in the output bundle. When using object destructuring with nested properties, some variables that should be available are missing from the compiled code.

### Reproduction

```js
const obj = {
  nested: {
    value: 42
  }
};

// Destructure with a property that has side effects in the key
const { [getKey()]: extracted } = obj;

function getKey() {
  console.log('Getting key');
  return 'nested';
}

console.log(extracted);
```

The destructured variable `extracted` should be properly included in the bundle, but it appears to be missing or incorrectly handled when the property key has side effects.

### Expected behavior

The destructured variables should be correctly included in the output, and the code should work as expected even when property keys have side effects (like function calls).

### Additional context

This seems to happen specifically when:
1. Using computed property names in destructuring
2. The property key expression has side effects
3. The value being destructured is not yet included in the bundle

The bundler appears to be making incorrect decisions about what code to include/exclude during tree-shaking.

---
Repository: /testbed
