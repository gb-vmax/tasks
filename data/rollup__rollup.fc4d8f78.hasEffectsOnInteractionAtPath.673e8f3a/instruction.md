# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where side effects are being incorrectly evaluated. When using logical operators (`&&`, `||`, `??`) in my code, the bundler seems to be making incorrect assumptions about whether expressions have side effects or not.

### Reproduction

```js
// Case 1: Logical OR with side effects
const result = sideEffectFunction() || anotherFunction();

// Case 2: Logical AND with side effects  
const value = obj.method() && obj.anotherMethod();

// Case 3: Nullish coalescing
const data = getValue() ?? getDefaultValue();
```

In all these cases, the bundler appears to be treating the side effects incorrectly - either removing code that should be kept, or keeping code that should be removed during tree-shaking.

### Expected behavior

The bundler should correctly identify when expressions in logical operations have side effects and preserve them accordingly. Functions with side effects should not be removed even if their return values aren't used.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The output bundles are either missing necessary function calls or including unnecessary ones.

---
Repository: /testbed
