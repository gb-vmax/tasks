# Bug Report

### Describe the bug

I'm experiencing an issue where sequence expressions (comma operator) are being incorrectly evaluated for side effects. When I have code with sequence expressions that clearly have side effects, Rollup is treating them as if they don't have any effects and removing them during tree-shaking.

### Reproduction

```js
// This code should be preserved because console.log has side effects
const result = (console.log('first'), console.log('second'), 42);

// But Rollup is removing the console.log calls during bundling
```

Another example:

```js
// Multiple expressions with side effects in a sequence
let x = 0;
const value = (x++, x++, x);
// The increments are being removed even though they have clear side effects
```

### Expected behavior

Sequence expressions containing side effects should be preserved during the bundling process. The tree-shaking algorithm should detect that expressions like `console.log()` or variable mutations have side effects and keep them in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as this was working correctly in previous versions. The comma operator should evaluate all expressions from left to right and any side effects should be preserved.

---
Repository: /testbed
