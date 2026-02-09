# Bug Report

### Describe the bug

Variables are not being marked as reassigned correctly. When `markReassigned()` is called on a variable, the `isReassigned` property doesn't get set to `true` as expected.

### Reproduction

```js
const variable = new Variable('myVar');

// Initially false
console.log(variable.isReassigned); // false

// Mark as reassigned
variable.markReassigned();

// Should be true, but remains false
console.log(variable.isReassigned); // false
```

### Expected behavior

After calling `markReassigned()`, the `isReassigned` property should be set to `true` so that the variable is properly tracked as having been reassigned.

### Additional context

This affects tree-shaking and dead code elimination since variables that are reassigned need to be handled differently than those that aren't. The current behavior causes variables to not be recognized as reassigned even after explicitly marking them.

---
Repository: /testbed
