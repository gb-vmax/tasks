# Bug Report

### Describe the bug

I'm encountering an issue where the export shim is being applied to chunks even when none of the modules actually need it. This seems to be happening incorrectly - the logic for determining when to add the exports shim appears to be inverted.

### Reproduction

```js
// Create a chunk with modules that don't need export shims
const chunk = new Chunk({
  // ... chunk configuration
});

// Add modules that have needsExportShim = false
chunk.orderedModules.push({
  needsExportShim: false,
  // ... other module properties
});

// The chunk incorrectly sets needsExportsShim to true
// even though no modules require it
```

### Expected behavior

The chunk should only set `needsExportsShim` to `true` when at least one of its ordered modules has `needsExportShim` set to `true`. Currently it seems to be doing the opposite - setting the shim when modules DON'T need it.

### Additional context

This is causing unnecessary export shim code to be added to the output bundle, which shouldn't be there. The shim should only be included when actually required by the modules in the chunk.

---
Repository: /testbed
