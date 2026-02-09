# Bug Report

### Describe the bug

I'm experiencing an issue where block statements are being incorrectly included in the output bundle. It seems like blocks that should be excluded are getting included anyway, causing unnecessary code to appear in the final build.

### Reproduction

```js
// Example code structure
if (false) {
  const unusedBlock = {
    // This block should be tree-shaken
    data: 'test'
  };
}
```

When bundling code with unreachable block statements, these blocks are appearing in the output even though they should be removed during tree-shaking. The condition is clearly false, so the entire block should be eliminated.

### Expected behavior

Block statements that are provably unreachable should be completely excluded from the bundle. Dead code elimination should remove these blocks during the build process.

### Additional context

This appears to be related to how block statement inclusion is being determined. The logic for checking whether a block is directly included might be inverted or not properly evaluating the flags.

---
Repository: /testbed
