# Bug Report

### Describe the bug

I'm experiencing an issue with if-else statement handling where the wrong branch is being included in the output. When an if statement has a known test value, the code appears to be including the opposite branch than what should be executed.

### Reproduction

```js
// Simple if-else with constant condition
if (true) {
  console.log('consequent');
} else {
  console.log('alternate');
}

// Expected: only 'consequent' branch should be in output
// Actual: 'alternate' branch is included instead
```

Similarly, when the condition is false:

```js
if (false) {
  console.log('consequent');
} else {
  console.log('alternate');
}

// Expected: only 'alternate' branch should be in output  
// Actual: 'consequent' branch is included instead
```

### Expected behavior

When an if statement has a statically known test value (like `true` or `false`), only the branch that would actually execute should be included in the bundled output. The dead code branch should be eliminated.

### Additional context

This seems to affect tree-shaking optimization. Code that should be removed as unreachable is being kept in the bundle, while code that should execute is being removed.

---
Repository: /testbed
