# Bug Report

### Describe the bug

I'm encountering an issue with multi-expression evaluation where side effects are not being properly detected. When I have a sequence of expressions (like in a comma operator), the last expression's side effects seem to be ignored during analysis.

### Reproduction

```js
// Example case: sequence expression with side effects
const code = `
  let x = 0;
  (console.log('first'), x++, console.log('last'));
`;

// The last console.log should be detected as having side effects
// but it appears to be skipped in the analysis
```

Another scenario:
```js
// When checking if expressions have effects
(sideEffect1(), sideEffect2(), finalExpression())

// The finalExpression's side effects are not being checked
```

### Expected behavior

All expressions in a multi-expression sequence should be analyzed for side effects, including the last one. Currently it seems like the final expression is being excluded from the side effect analysis, which could lead to incorrect tree-shaking or optimization decisions.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with proper dead code elimination in my build. Any expressions in the last position of a sequence are not having their effects properly tracked.

---
Repository: /testbed
