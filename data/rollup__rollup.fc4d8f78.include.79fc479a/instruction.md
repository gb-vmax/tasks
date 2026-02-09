# Bug Report

### Describe the bug

I'm encountering an issue with while loops where the loop body isn't being included correctly in the bundle. It seems like the body of while statements is not being processed with the right inclusion flags, which causes parts of the code inside the loop to be incorrectly tree-shaken or not included at all.

### Reproduction

```js
// input.js
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```

When bundling this code, the while loop body doesn't get included properly in the output. The expected behavior is that the entire loop body should be preserved, but instead it seems like child nodes within the loop aren't being included recursively when they should be.

### Expected behavior

The while loop body should be fully included in the bundle output with all its child nodes properly processed. When `includeChildrenRecursively` is true for the while statement, it should propagate to the loop body as well.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
