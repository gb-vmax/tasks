# Bug Report

### Describe the bug

I'm experiencing an issue with `continue` statements inside loops when they have labels. The code behaves incorrectly - it seems like the control flow analysis is inverted for labeled continue statements.

### Reproduction

```js
function testLabeledContinue() {
  outer: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (j === 1) {
        continue outer;
      }
      console.log(i, j);
    }
  }
}
```

When using a labeled `continue` statement like `continue outer;`, the bundler seems to treat it incorrectly during tree-shaking or dead code elimination. Code that should be removed is being kept, or vice versa.

### Expected behavior

Labeled continue statements should properly signal control flow breaks to the outer labeled loop. The static analysis should correctly identify which code paths are reachable after a labeled continue.

### Additional context

This appears to be related to how the AST handles control flow for continue statements with labels vs unlabeled continues. The logic seems reversed - when a label is present and matches an ignored label, it's being treated as having effects when it shouldn't (or the other way around).

---
Repository: /testbed
