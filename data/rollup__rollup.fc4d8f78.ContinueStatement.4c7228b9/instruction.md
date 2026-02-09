# Bug Report

### Describe the bug

I'm encountering an issue with `continue` statements in loops being incorrectly removed during tree-shaking/dead code elimination. When a `continue` statement appears in my code, it gets stripped out even though it's clearly reachable and should be included in the final bundle.

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
```

After bundling, the `continue` statement is missing from the output, which breaks the logic of the loop. The code should skip certain iterations but instead processes all items.

### Expected behavior

The `continue` statement should be preserved in the bundled output when it's part of reachable code. The tree-shaking algorithm should recognize that unlabeled `continue` statements are necessary for control flow within loops.

### Additional context

This seems to affect unlabeled `continue` statements specifically. Labeled continues might work differently but I haven't tested those extensively.

---
Repository: /testbed
