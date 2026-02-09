# Bug Report

### Describe the bug

I'm experiencing issues with update expressions (like `++` and `--`) when used with exported variables in the system format. The behavior seems incorrect when dealing with prefix increment/decrement operators on variables that are exported.

### Reproduction

```js
// module.js
export let counter = 0;

// This doesn't work as expected
++counter;

// The export statement isn't being handled correctly
```

When using prefix update expressions on exported variables, the generated code doesn't properly handle the system module format exports. This appears to affect how the variable updates are tracked and exported.

### Expected behavior

Prefix increment/decrement operators should correctly update exported variables and generate proper system format export statements. The variable should be updated and the export should reflect the new value.

### Additional context

This seems to be related to how the bundler handles update expressions when they interact with the module system. The issue specifically manifests when:
1. Using prefix operators (`++x` or `--x`) 
2. On variables that are exported
3. In system module format

The postfix operators might be affected differently, but the prefix case is definitely broken.

---
Repository: /testbed
