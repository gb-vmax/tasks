# Bug Report

### Describe the bug

I'm experiencing an issue where the first statement in a block is being skipped during code generation. When I have multiple statements in a block, only statements after the first one are included in the output bundle.

### Reproduction

```js
{
  const first = 'this gets skipped';
  const second = 'this is included';
  const third = 'this is also included';
}
```

After bundling, only `second` and `third` appear in the output, while `first` is completely missing.

This seems to affect any block statement - function bodies, if statements, etc. The first statement/declaration in the block just disappears from the final bundle.

### Expected behavior

All statements in a block should be included in the output, not just those after the first one.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
