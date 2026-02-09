# Bug Report

### Describe the bug

Dynamic imports are not being included in the bundle output. When using `import()` expressions in the code, they seem to be completely ignored during the build process and don't appear in the final bundle.

### Reproduction

```js
// main.js
async function loadModule() {
  const module = await import('./dynamic-module.js');
  return module.default;
}

loadModule();
```

After bundling, the dynamic import is not present in the output and the module is not loaded at runtime.

### Expected behavior

Dynamic imports should be properly tracked and included in the bundle. The `import()` expression should be preserved (or transformed appropriately) in the output so that the module can be loaded dynamically at runtime.

### Additional context

This seems to affect all dynamic import statements regardless of whether they use string literals or template expressions. The bundler appears to be skipping these imports entirely rather than processing them correctly.

---
Repository: /testbed
