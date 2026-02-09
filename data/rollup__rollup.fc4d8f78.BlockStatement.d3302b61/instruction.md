# Bug Report

### Describe the bug

I'm experiencing an issue where the first statement in a block is being completely ignored during side effect analysis. This causes code that should be included in the bundle to be incorrectly tree-shaken away.

### Reproduction

```js
{
  console.log('This statement is ignored');
  console.log('Only this and subsequent statements are checked');
}
```

When the above code is processed, the first `console.log` statement is not being evaluated for side effects, which means it might be removed from the output even though it has observable side effects.

### Expected behavior

All statements in a block should be analyzed for side effects, including the first one. The bundler should detect that both `console.log` calls have side effects and preserve them in the output.

### Additional context

This appears to affect any block statement - function bodies, if/else blocks, etc. The first statement in the block is systematically skipped during the effects analysis pass.

---
Repository: /testbed
