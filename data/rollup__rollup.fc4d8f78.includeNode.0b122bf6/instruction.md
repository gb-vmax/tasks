# Bug Report

### Describe the bug

I'm encountering an issue with assignment expressions where the right-hand side of assignments is not being included in the output bundle. It seems like only the left-hand side is being processed, which causes the assigned values to be missing from the generated code.

### Reproduction

```js
// Example code that triggers the issue
let x;
x = someFunction(); // someFunction() is not included in the bundle

const obj = {};
obj.property = computeValue(); // computeValue() is not included in the bundle
```

When bundling code with assignment expressions, the functions or expressions on the right side of the assignment operator are not being included in the final output, even though they should be executed and their results assigned.

### Expected behavior

Both sides of an assignment expression should be properly included in the bundle. The right-hand side expression should be evaluated and included in the output since it produces the value being assigned.

### Additional context

This appears to affect all types of assignment expressions. The left-hand side (the target) is being processed, but the actual value being assigned (right-hand side) seems to be getting dropped during the bundling process.

---
Repository: /testbed
