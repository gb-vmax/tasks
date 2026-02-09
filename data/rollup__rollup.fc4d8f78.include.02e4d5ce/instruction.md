# Bug Report

### Describe the bug

I'm encountering an issue with labeled statements in my code. When using a labeled statement with a `break` that references the label, the label itself is being incorrectly included in the output even when the break statement is removed during tree-shaking.

### Reproduction

```js
// Input code
function test() {
  myLabel: {
    if (false) {
      break myLabel;
    }
    console.log('executed');
  }
}
```

In this case, since the `if (false)` condition is always false, the `break myLabel;` statement should be removed during dead code elimination. When this happens, the label `myLabel:` should also be removed from the output since it's no longer referenced.

However, the label is being kept in the bundled output even though there's no break statement referencing it anymore.

### Expected behavior

When a labeled statement's label is not referenced by any break/continue statements (after tree-shaking removes unreachable code), the label itself should be removed from the output, leaving just the block statement contents.

Expected output after tree-shaking:
```js
function test() {
  {
    console.log('executed');
  }
}
```

### Additional context

This appears to be related to how the inclusion logic handles labeled statements and their references. The label should only be included if there's an actual break/continue statement that references it in the included code.

---
Repository: /testbed
