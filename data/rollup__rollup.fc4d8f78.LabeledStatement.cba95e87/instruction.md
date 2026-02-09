# Bug Report

### Describe the bug

Labeled statements are being included in the output even when they shouldn't be. It seems like the logic for determining when to include a label is inverted - labels are being kept when there's no reference to them, and potentially removed when they are actually used.

### Reproduction

```js
// Example code with labeled statement
function test() {
  myLabel: {
    console.log('inside label');
    // No break statement referencing myLabel
  }
  console.log('after label');
}
```

When bundling code like this, the label `myLabel:` appears in the output even though nothing references it (no `break myLabel` statements). The label should be removed during tree-shaking since it's not being used.

### Expected behavior

Unreferenced labels should be removed from the output during the tree-shaking process. Only labels that are actually referenced (e.g., by `break` or `continue` statements) should be preserved in the final bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
