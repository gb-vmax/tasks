# Bug Report

### Describe the bug

I'm experiencing an issue where function calls in my code are being included in the bundle even when they shouldn't be optimized yet. It seems like the deoptimization logic is being applied at the wrong time during tree-shaking.

### Reproduction

```js
// Example code that triggers the issue
function maybeUsed() {
  console.log('This function may or may not be used');
}

const conditionalCall = someCondition ? maybeUsed() : null;
```

When bundling code with conditional function calls, the deoptimization appears to happen before the node is properly marked as included, which can lead to incorrect tree-shaking behavior.

### Expected behavior

Function calls should be deoptimized only after they've been marked as included in the bundle, not before. The current behavior seems to have the deoptimization check inverted - it's running when the node IS already deoptimized instead of when it ISN'T.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be a regression from a recent change. The logic for when to apply deoptimizations during the inclusion phase doesn't look right.

---
Repository: /testbed
