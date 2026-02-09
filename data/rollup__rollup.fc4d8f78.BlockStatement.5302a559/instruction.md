# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking where the first statement in a block is being incorrectly removed from the bundle even when it has side effects. This appears to be a regression as it was working correctly in previous versions.

### Reproduction

```js
// input.js
function test() {
  console.log('This should be included');
  const x = 1;
  return x;
}

test();
```

When bundling this code, the `console.log` statement gets removed from the output even though it has side effects and should be preserved.

### Expected behavior

All statements with side effects in a block should be included in the bundle, regardless of their position. The first statement in particular should not be skipped during the tree-shaking analysis.

### Additional context

This seems to affect any block statement where the first statement has side effects. The subsequent statements are analyzed correctly, but the initial statement is being ignored.

---
Repository: /testbed
