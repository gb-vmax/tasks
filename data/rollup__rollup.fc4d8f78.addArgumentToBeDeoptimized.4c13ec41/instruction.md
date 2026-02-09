# Bug Report

### Describe the bug

I'm encountering an issue where function argument deoptimization is not working as expected. When passing valid arguments to functions, they're not being properly tracked for deoptimization, which causes incorrect optimization behavior in the bundler.

### Reproduction

```js
function example(arg) {
  // arg should be deoptimized when needed
  return arg.someProperty;
}

// This should trigger argument deoptimization
const result = example({ someProperty: 'value' });
```

When building code with function arguments that should be deoptimized, the bundler doesn't handle them correctly. It seems like valid arguments are being skipped during the deoptimization process.

### Expected behavior

All function arguments should be properly registered for deoptimization when needed, regardless of their value. The bundler should track these arguments to ensure correct optimization decisions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
