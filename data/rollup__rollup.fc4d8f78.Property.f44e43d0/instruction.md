# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignments where properties aren't being included correctly in the output. It seems like when destructuring objects, certain properties that should be included are being left out, causing the bundled code to break.

### Reproduction

```js
const obj = {
  computed: true,
  value: { x: 1 }
};

// Destructure with a computed property key
const { [key]: value } = obj;
```

When bundling code that uses destructuring with computed property keys, the necessary properties aren't being tracked properly. The bundler seems to be incorrectly determining which parts of the destructuring assignment need to be included in the final output.

### Expected behavior

All properties involved in destructuring assignments should be properly included in the bundled output, regardless of whether they use computed property keys or static keys. The code should work the same way after bundling as it does before.

### Additional context

This appears to affect destructuring patterns in various contexts - variable declarations, function parameters, etc. The issue is particularly noticeable when using computed property keys in the destructuring pattern.

---
Repository: /testbed
