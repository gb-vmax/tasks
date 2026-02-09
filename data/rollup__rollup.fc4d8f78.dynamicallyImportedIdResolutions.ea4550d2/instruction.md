# Bug Report

### Describe the bug

I'm encountering an issue with dynamically imported modules where the `dynamicallyImportedIdResolutions` getter is returning incorrect or empty results. It seems like the resolution logic isn't properly accessing the module IDs from dynamic imports.

### Reproduction

```js
// Setup a module with dynamic imports
const module = {
  resolvedIds: {
    './foo.js': { id: './foo.js', external: false },
    './bar.js': { id: './bar.js', external: false }
  }
};

const dynamicImports = [
  { argument: './foo.js' },
  { argument: './bar.js' }
];

// When accessing dynamicallyImportedIdResolutions
// Expected: Array of resolved IDs
// Actual: Empty array or undefined values
```

### Expected behavior

The `dynamicallyImportedIdResolutions` should return an array of resolved module IDs for all string-based dynamic imports. Each resolved ID should correctly map to the corresponding entry in `module.resolvedIds`.

### Additional context

This appears to be related to how dynamic import arguments are being filtered and mapped. The getter should be able to properly extract string arguments from dynamic imports and look them up in the resolved IDs map.

---
Repository: /testbed
