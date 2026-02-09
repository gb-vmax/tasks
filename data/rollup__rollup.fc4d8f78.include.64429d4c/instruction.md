# Bug Report

### Describe the bug

I'm encountering an issue with labeled statements in my code. When using break statements with labels, the label itself is being included in the output even when it's not actually being referenced by any break statement.

### Reproduction

```js
function test() {
  myLabel: {
    console.log('inside label');
    // No break statement referencing myLabel
  }
}
```

In this case, the label `myLabel` should be removed from the output during tree-shaking since there's no break statement that references it. However, the label is still present in the bundled output.

### Expected behavior

Labels should only be included in the final bundle when they are actually referenced by a break or continue statement. Unreferenced labels should be removed during the tree-shaking process.

### Additional context

This seems to affect code where labeled statements are used but the label itself is never targeted by control flow statements. The bundler should be smart enough to remove these unused labels.

---
Repository: /testbed
