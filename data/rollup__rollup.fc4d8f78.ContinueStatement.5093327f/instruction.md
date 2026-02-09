# Bug Report

### Describe the bug

I'm encountering an issue with labeled `continue` statements in my code. When using a `continue` statement with a label inside a loop, the bundler is incorrectly treating it as having side effects and including code that should be tree-shaken away.

### Reproduction

```js
function test() {
  outer: for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
      if (j === 5) {
        continue outer;
      }
      console.log(i, j);
    }
  }
}

// This function should be removed during tree-shaking
// but it's being kept in the bundle
function unused() {
  myLabel: while (true) {
    if (Math.random() > 0.5) {
      continue myLabel;
    }
    break;
  }
}
```

### Expected behavior

Labeled continue statements should be handled correctly during the tree-shaking process. Code with labeled continues that is not referenced should be removed from the final bundle, just like regular continue statements.

### Additional context

This seems to affect how the bundler analyzes control flow with labeled statements. The behavior is inconsistent between labeled and unlabeled continue statements.

---
Repository: /testbed
