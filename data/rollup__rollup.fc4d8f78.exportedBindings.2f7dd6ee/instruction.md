# Bug Report

### Describe the bug

I'm experiencing an issue with `export *` statements in my modules. When I use `export * from './module'`, the exported bindings information seems to be incorrect. Instead of getting the wildcard marker `'*'` as expected, I'm seeing the source module path duplicated in the bindings.

### Reproduction

```js
// module-a.js
export const foo = 1;
export const bar = 2;

// module-b.js
export * from './module-a';

// When inspecting exportedBindings for module-b:
// Expected: { './module-a': ['*'] }
// Actual: { './module-a': ['./module-a'] }
```

This is causing issues when trying to analyze the module graph and understand which modules are re-exporting all bindings from other modules.

### Expected behavior

When using `export * from 'source'`, the `exportedBindings` should contain `'*'` in the array for that source, not the source path itself.

### Additional context

This seems to affect how re-exports are tracked. The wildcard export marker should be consistent with how other parts of the system expect it to be represented.

---
Repository: /testbed
