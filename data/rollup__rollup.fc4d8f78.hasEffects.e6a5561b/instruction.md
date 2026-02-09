# Bug Report

### Describe the bug

I'm encountering an issue with do-while loops where side effects are not being detected correctly. It seems like the tree-shaking is removing code that should be kept because it has side effects.

### Reproduction

```js
// This do-while loop has side effects but gets incorrectly tree-shaken
let x = 0;
do {
  console.log('This should be included');
  x++;
} while (x < 5);
```

The loop body contains `console.log` which is a side effect, but the code is being removed during the build process. This is causing my application to behave incorrectly as important side effects are being stripped out.

### Expected behavior

Do-while loops with side effects in their body should be preserved in the output bundle. The loop body should be analyzed for side effects and if any are found, the entire statement should be included.

### Additional context

This appears to be related to how do-while statements are being analyzed. The issue specifically affects do-while loops - regular while loops seem to work fine.

---
Repository: /testbed
