# Bug Report

### Describe the bug

I'm encountering an issue with side effect detection in multi-expression scenarios. When analyzing expressions that contain multiple sub-expressions (like in sequence expressions or comma operators), the side effect analysis seems to be returning incorrect results.

The problem appears when checking if an interaction has effects - it's not properly evaluating all expressions in the sequence. If any expression in the middle doesn't have effects, the entire check returns false prematurely, even if other expressions do have effects.

### Reproduction

```js
// Example with sequence expression
const code = `
  (foo(), bar(), baz())
`;

// If bar() has no side effects but foo() and baz() do,
// the analysis incorrectly reports no side effects overall
```

This affects tree-shaking and dead code elimination, potentially causing code with side effects to be incorrectly removed or vice versa.

### Expected behavior

The side effect analysis should correctly identify when ANY expression in a multi-expression has effects, not just return false when encountering the first expression without effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
