# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring patterns where properties with computed keys are not being properly included in the output. It seems like the inclusion logic for destructured properties is not working as expected.

### Reproduction

```js
const obj = {
  [computedKey]: value
};

const { [computedKey]: extracted } = obj;
```

When using destructuring with computed property keys, the key effects are not being evaluated correctly and the property is not included in the bundle when it should be.

### Expected behavior

Destructured properties with computed keys should be properly included in the output bundle when they have side effects or are used in the code. The key's effects should be checked and the property should be included accordingly.

### Additional context

This seems to affect cases where:
- Destructuring uses computed property names
- The key expression has side effects
- The property needs to be included based on the key's effects

The issue appears to be related to how the inclusion logic handles the combination of computed keys and destructured properties.

---
Repository: /testbed
