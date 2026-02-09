# Bug Report

### Describe the bug

I'm experiencing an issue with unary expressions not being properly optimized during tree-shaking. When I use unary operators like `!`, `+`, or `-` with literal values, the bundler seems to be including code that should be eliminated.

### Reproduction

```js
// Input code
const result = !true;
const num = +42;
const neg = -5;

console.log(result, num, neg);
```

When bundling this code, I expected the unary expressions with literal values to be evaluated and optimized at build time, but they're being left in the output bundle unchanged. This is causing unnecessary code to remain in the production build.

### Expected behavior

The bundler should evaluate unary expressions with literal values during the build process and replace them with their computed values. For example:
- `!true` should become `false`
- `+42` should become `42`
- `-5` should become `-5`

This was working correctly in previous versions, but seems to have regressed recently.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
