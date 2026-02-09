# Bug Report

### Describe the bug

I'm experiencing an issue where empty blocks or blocks with statements are not being evaluated correctly for side effects. It seems like the tree-shaking behavior has changed and code that should be removed is now being kept in the bundle, or vice versa.

### Reproduction

```js
// Case 1: Empty block with side effects
{
  // This block should be considered to have effects in certain contexts
  // but appears to be incorrectly evaluated
}

// Case 2: Block with statements
{
  console.log('test');
  someFunction();
}
```

When bundling code with these patterns, the output is unexpected. Blocks that should be included are being removed, or blocks that should be removed are being kept.

### Expected behavior

The bundler should correctly determine whether a block statement has side effects based on:
1. Whether the block body contains statements with effects
2. The deoptimization state of the block
3. The control flow context (whether flow has been broken)

Blocks with side effects should be preserved in the output, while pure blocks should be tree-shaken appropriately.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
