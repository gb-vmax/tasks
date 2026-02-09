# Bug Report

### Describe the bug

Variable declarators are being rendered incorrectly when they're not included in the output. The logic for determining whether to render the identifier appears to be inverted, causing variables to be removed when they should be kept and vice versa.

### Reproduction

```js
// When bundling code with tree-shaking enabled
const unusedVar = someValue;
export const usedVar = anotherValue;

// The unused variable declaration is being rendered incorrectly
// Expected: the unused parts should be removed cleanly
// Actual: the rendering logic removes the wrong parts
```

### Expected behavior

When a variable declarator's identifier is included in the output (or when using `using`/`await using` declarations), it should render the identifier normally. When it's not included, the declarator should be removed properly by finding the assignment operator and removing everything up to the initialization value.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
