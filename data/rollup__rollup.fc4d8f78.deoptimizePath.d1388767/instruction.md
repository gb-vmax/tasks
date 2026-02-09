# Bug Report

### Describe the bug

I'm experiencing incorrect tree-shaking behavior with logical expressions (`&&`, `||`, `??`). When a logical expression has a determinable branch at compile time, properties accessed on the unused branch are still being included in the bundle instead of being tree-shaken away.

### Reproduction

```js
const obj = {
  usedProp: 'used',
  unusedProp: 'unused'
};

// When condition is known to be truthy at build time
const result = true && obj.usedProp || obj.unusedProp;

// Expected: only obj.usedProp should be in the bundle
// Actual: both obj.usedProp and obj.unusedProp are included
```

Another example:

```js
const config = {
  dev: { /* ... */ },
  prod: { /* ... */ }
};

// When NODE_ENV is replaced with 'production' at build time
const settings = false && config.dev || config.prod;

// Expected: config.dev should be tree-shaken away
// Actual: config.dev is still included in the bundle
```

### Expected behavior

When a logical expression's branch can be determined at compile time (e.g., through constant folding), only the properties accessed on the used branch should be included in the final bundle. Properties accessed on the unused branch should be tree-shaken away.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to be a regression as it was working correctly in previous versions. The bundle size is significantly larger than expected due to dead code not being eliminated properly.

---
Repository: /testbed
