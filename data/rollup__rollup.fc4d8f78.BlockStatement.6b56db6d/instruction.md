# Bug Report

### Describe the bug

I'm experiencing an issue where block statements with effects are not being handled correctly during tree-shaking. Specifically, when a block contains statements that should be evaluated for side effects, some code that should be included in the output is being incorrectly removed.

### Reproduction

```js
// input.js
function test() {
  {
    console.log('This should be included');
    return;
    console.log('This should be excluded');
  }
}

test();
```

When bundling this code, the block statement's content is not being properly analyzed for effects. The issue seems related to how broken control flow (like `return` statements) is being handled within block scopes.

### Expected behavior

The bundler should correctly identify which statements have side effects and include them in the output, even when they appear in block statements. Statements after control flow breaks (like `return`) should be properly excluded, but statements before the break should be included if they have effects.

### Additional context

This appears to affect code that uses block statements with early returns or other control flow modifications. The tree-shaking logic seems to be checking conditions in the wrong order or with incorrect logic operators when determining what to include.

---
Repository: /testbed
