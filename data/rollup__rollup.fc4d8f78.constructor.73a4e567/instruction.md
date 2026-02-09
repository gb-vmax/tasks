# Bug Report

### Describe the bug

The `importers` getter in the module info object is not returning a sorted array. This causes inconsistent ordering when accessing the importers property on external modules, which can lead to unpredictable behavior in code that relies on a consistent ordering.

### Reproduction

```js
// Create an external module with multiple importers
const externalModule = new ExternalModule(
  options,
  'my-external-module',
  true,
  {},
  false,
  {}
);

// Add importers in different order
externalModule.importers.push('module-b');
externalModule.importers.push('module-a');
externalModule.importers.push('module-c');

// Access the importers through the info object
console.log(externalModule.info.importers);
// Expected: ['module-a', 'module-b', 'module-c']
// Actual: ['module-b', 'module-a', 'module-c']
```

The importers are returned in insertion order rather than sorted order. This is inconsistent with the `dynamicImporters` getter which does return a sorted array.

### Expected behavior

The `importers` property should return a sorted array to ensure consistent and predictable ordering, matching the behavior of `dynamicImporters`.

---
Repository: /testbed
