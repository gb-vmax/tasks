# Bug Report

### Describe the bug

I'm experiencing an issue where MDX syntax extensions are not being fully applied when multiple extensions are passed. It seems like the last extension in the array is being skipped during processing.

### Reproduction

```js
const extensions = [
  extensionA,
  extensionB,
  extensionC
];

const result = combineExtensions(extensions);
// extensionC is not included in the result
```

When I pass an array of 3 extensions, only the first 2 are actually combined. The last one in the array doesn't get processed at all.

### Expected behavior

All extensions in the array should be combined and applied, including the last one.

### Additional context

This appears to affect any scenario where multiple syntax extensions need to be combined. The issue is consistent - it's always the last extension that gets dropped.

---
Repository: /testbed
