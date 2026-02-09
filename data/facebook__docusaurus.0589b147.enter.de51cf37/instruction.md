# Bug Report

### Describe the bug
I'm encountering an issue with directive parsing where the arguments to `this.enter()` appear to be in the wrong order. When processing text directives, the token and node object seem to be swapped, which is causing directives to not be parsed correctly.

### Reproduction
```js
// When parsing a text directive like :directive[content]
// The enter function is called but arguments are reversed

const directive = ':example[test content]';
// Parse this directive
// Expected: Should create proper directive node
// Actual: Arguments passed to enter() are swapped
```

### Expected behavior
The `enter()` function should receive the node object as the first argument and the token as the second argument, consistent with the micromark extension API. Directives should be parsed correctly with their type, name, attributes, and children properties properly initialized.

### Additional context
This affects text directives, leaf directives, and container directives since they all use the same `enter()` helper function. The node structure gets corrupted because the token is being passed where the node object should be.

---
Repository: /testbed
