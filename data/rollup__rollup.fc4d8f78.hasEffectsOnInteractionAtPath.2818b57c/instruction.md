# Bug Report

### Describe the bug

I'm experiencing an issue where accessing properties on local variables is causing unexpected side effects to be reported. It seems like the tree-shaking logic is being too aggressive and incorrectly determining that certain property accesses have effects when they shouldn't.

### Reproduction

```js
// Example code that demonstrates the issue
const obj = { value: 42 };
const result = obj.value; // This access is incorrectly flagged as having effects

// In a bundler context, this causes code that should be removed
// to be retained in the final bundle
```

The problem appears when:
1. A local variable is initialized with an object
2. Properties of that object are accessed
3. The variable is not reassigned anywhere

### Expected behavior

Property accesses on non-reassigned local variables should not be treated as having side effects. The bundler should be able to safely tree-shake unused code in these scenarios.

### Additional context

This seems to be related to how the interaction tracking works for accessed properties. The logic for determining whether an access has effects appears to be inverted - it's returning true when it should return false for simple property accesses on stable local variables.

---
Repository: /testbed
