# Bug Report

### Describe the bug

I'm encountering an issue where for-loop statements are being incorrectly excluded from the bundled output. When I have a for-loop in my code, it seems like the entire loop is getting tree-shaken out even though it should be included.

### Reproduction

```js
// Input code
function processItems(items) {
  for (let i = 0; i < items.length; i++) {
    console.log(items[i]);
  }
}

processItems([1, 2, 3]);
```

After bundling, the for-loop is missing from the output. The function body appears to be empty or the loop is completely removed.

### Expected behavior

The for-loop should be preserved in the bundled output since it contains side effects (console.log). The code should execute normally and not have the loop stripped out during the build process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
