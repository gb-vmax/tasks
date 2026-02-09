# Bug Report

### Describe the bug

Dynamic imports with inline namespaces are not being included in the generated output when they should be. After a recent change, it seems like the namespace variables from dynamic imports are being incorrectly filtered out, causing them to be missing from the final bundle.

### Reproduction

```js
// module.js
export const value = 42;

// main.js
async function loadModule() {
  const ns = await import('./module.js');
  console.log(ns.value);
}
```

When bundling this code with inlining enabled, the namespace variable that should be generated for the dynamic import is missing from the output, causing runtime errors.

### Expected behavior

The namespace variable for the dynamic import should be included in the bundled output regardless of whether it was previously tracked in `usedNames`. All inline namespaces from dynamic imports should be added to the used names set.

### Additional context

This appears to be related to how dynamic import namespaces are being tracked. The namespace variables seem to only be added if they already exist in the `usedNames` set, which doesn't make sense for new dynamic imports.

---
Repository: /testbed
