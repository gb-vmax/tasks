# Bug Report

### Describe the bug

When using SystemJS output format with multiple export names for the same variable, the wrong export name is being used in the generated code. It appears that the second export name is being selected instead of the first one.

### Reproduction

```js
// Input code with aliased exports
export { foo as bar };
export { foo as baz };

// Expected SystemJS output should use 'bar' (first export name)
// But actual output uses 'baz' (second export name)
```

### Expected behavior

When a variable has multiple export names, the SystemJS format should use the first export name in the `exports()` call, not a different one from the array.

### Additional context

This affects the correctness of the generated SystemJS bundles when variables are exported under multiple names. The wrong export name being used could break module loading in SystemJS environments.

---
Repository: /testbed
