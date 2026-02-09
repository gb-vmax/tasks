# Bug Report

### Describe the bug

When tree-shaking function calls with multiple arguments where only some arguments are included, the first argument is being skipped during rendering. This causes the generated code to be missing the first argument even when it should be included.

### Reproduction

```js
// Input code with a function call where middle arguments are tree-shaken
someFunction(arg1, unusedArg2, arg3);

// After tree-shaking with arg2 removed, expected output:
someFunction(arg1, arg3);

// Actual output (first argument missing):
someFunction(arg3);
```

This happens when:
1. A function has multiple arguments
2. Some arguments in the middle are marked as not included (tree-shaken out)
3. The first argument is included but gets skipped during rendering

### Expected behavior

All included arguments should be rendered in the output, including the first argument when it's marked as included. The rendering logic should iterate from index 0, not skip the first argument.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
