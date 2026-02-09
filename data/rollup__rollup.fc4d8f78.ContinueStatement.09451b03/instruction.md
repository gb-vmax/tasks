# Bug Report

### Describe the bug

I'm encountering an issue with `continue` statements inside loops where code after the `continue` statement is being incorrectly included in the bundle. It seems like the tree-shaking logic isn't properly recognizing that code following a `continue` statement is unreachable.

### Reproduction

```js
function example() {
  for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
      continue;
    }
    console.log('This should not be included for even numbers');
    // Some code here that should be recognized as unreachable after continue
    someUnusedFunction(); // This gets included even though it's unreachable
  }
}
```

Similarly with labeled continue statements:

```js
outer: for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 5; j++) {
    if (j === 2) {
      continue outer;
    }
    unreachableCode(); // This is being included in the output
  }
}
```

### Expected behavior

Code that appears after a `continue` statement should be marked as unreachable and excluded from the bundle during tree-shaking, just like code after `return` or `break` statements.

### Additional context

This appears to affect both labeled and unlabeled `continue` statements. The bundler doesn't seem to recognize that the control flow is broken after the `continue`, leading to dead code being included in the final output.

---
Repository: /testbed
