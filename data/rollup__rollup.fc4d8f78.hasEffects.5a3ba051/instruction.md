# Bug Report

### Describe the bug

I'm encountering an issue with tagged template expressions where the first expression in the template literal is not being evaluated for side effects. This causes the bundler to incorrectly tree-shake code that should be kept.

### Reproduction

```js
// This code gets incorrectly optimized
const result = myTag`prefix ${sideEffectFunction()} middle ${anotherFunction()} end`;

// The first expression (sideEffectFunction) is skipped during side effect analysis
// Only expressions after the first one are being checked
```

When bundling code with tagged templates, if the first expression has side effects (like a function call that modifies global state), those side effects are not being detected. This results in the code being removed during tree-shaking even though it should be preserved.

### Expected behavior

All expressions within a tagged template literal should be checked for side effects, including the first expression at index 0. The bundler should preserve any tagged template expression where any of its expressions have side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
