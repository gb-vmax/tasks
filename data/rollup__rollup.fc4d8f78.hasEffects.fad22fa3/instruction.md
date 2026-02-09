# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking where `continue` statements in loops are being incorrectly removed during the build process. Code that should be preserved is being eliminated, causing the bundled output to behave differently from the source code.

### Reproduction

```js
function processItems(items) {
  for (let i = 0; i < items.length; i++) {
    if (items[i].skip) {
      continue;
    }
    console.log(items[i]);
  }
}

processItems([
  { value: 1, skip: false },
  { value: 2, skip: true },
  { value: 3, skip: false }
]);
```

When bundled, the `continue` statement seems to be treated as having side effects when it shouldn't, or vice versa. The resulting bundle either includes unnecessary code or removes code that should be kept.

### Expected behavior

The `continue` statement should be properly analyzed for side effects. Unlabeled `continue` statements inside loops should be handled correctly and the bundled code should behave identically to the source.

### Additional context

This appears to affect unlabeled `continue` statements specifically. The logic for determining whether the statement has effects seems to be inverted in some cases.

---
Repository: /testbed
