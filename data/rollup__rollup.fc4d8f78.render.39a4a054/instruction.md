# Bug Report

### Describe the bug

I'm experiencing an issue with assignment expressions where the left-hand side is being rendered incorrectly when it should be excluded from the output. It seems like the inclusion logic is inverted - when the left side is included, it's being treated as if it's excluded, and vice versa.

### Reproduction

```js
// When you have an assignment expression where the left side should be tree-shaken
const result = (unusedVar = someValue);

// The output incorrectly renders the left side even though it's not used
// Expected: just the right-hand side value
// Actual: the full assignment is rendered when it shouldn't be
```

This affects dead code elimination and can result in bloated output bundles. The assignment expression rendering appears to have the condition backwards.

### Expected behavior

When the left-hand side of an assignment is not included (tree-shaken out), only the right-hand side should be rendered. When the left-hand side IS included, both sides should render normally.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
