# Bug Report

### Describe the bug

I'm experiencing an issue with member expression assignments where the assigned value and object are being passed in the wrong order during assignment interactions. This is causing unexpected behavior when tracking property assignments.

### Reproduction

```js
const obj = { prop: 'initial' };

// Assigning a new value to a property
obj.prop = 'new value';

// The assignment interaction receives arguments in wrong order
// Expected: [object, value]
// Actual: [value, object]
```

### Expected behavior

When a member expression is assigned a value, the assignment interaction should receive the object as the first argument and the assigned value as the second argument. Currently they appear to be reversed.

### Additional context

This seems to affect how assignment tracking works internally. The order of arguments matters for proper deoptimization and side effect analysis.

---
Repository: /testbed
