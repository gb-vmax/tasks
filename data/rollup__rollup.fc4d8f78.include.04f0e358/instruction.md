# Bug Report

### Describe the bug

Labels are not being included in the output when they are referenced by `break` or `continue` statements. The label gets removed from the bundle even though it's actively being used by control flow statements.

### Reproduction

```js
function test() {
  outer: for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (j === 2) {
        break outer;
      }
    }
  }
}
```

When bundling this code, the `outer:` label is stripped from the output, which breaks the `break outer;` statement. The bundled code ends up with just `break;` which has different semantics.

### Expected behavior

The label should be preserved in the output when it's referenced by a break or continue statement. The bundled code should maintain the same control flow behavior as the original.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
