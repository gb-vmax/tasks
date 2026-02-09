# Bug Report

### Describe the bug

Arrow functions are being treated as having side effects even when they shouldn't. This causes unnecessary inclusion of arrow function expressions in the bundle, leading to bloated output and incorrect tree-shaking behavior.

### Reproduction

```js
// This arrow function has no side effects but is still included in the bundle
const noop = () => {};

// Even pure arrow functions are not being removed during tree-shaking
const pureFunc = () => 42;

export { noop, pureFunc };
```

When bundling this code, both arrow functions are included in the output even though they have no side effects and are never used. This wasn't happening in previous versions.

### Expected behavior

Arrow functions without side effects should be correctly identified and removed during tree-shaking when they're not used. The bundler should recognize that these functions are pure and can be safely eliminated.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
