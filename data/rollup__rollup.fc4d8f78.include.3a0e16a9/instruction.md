# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions in my code. When I have a sequence expression with multiple comma-separated values, the last expression in the sequence is not being included in the output bundle. This causes runtime errors because the final value that should be returned is missing.

### Reproduction

```js
// Input code
const result = (sideEffect1(), sideEffect2(), finalValue);
console.log(result);

// After bundling, the finalValue is missing from the output
// This causes result to be undefined
```

Another example:
```js
// This should execute all three expressions and return the last one
export const value = (doSetup(), initialize(), computedResult);

// But computedResult is not included in the bundle
```

### Expected behavior

All expressions in a sequence should be evaluated, and the last expression should be included in the output as it represents the final value of the sequence expression. The bundler should not drop the last expression.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The second-to-last expression is being treated as if it's the final one, which breaks code that relies on sequence expressions returning their last value.

---
Repository: /testbed
