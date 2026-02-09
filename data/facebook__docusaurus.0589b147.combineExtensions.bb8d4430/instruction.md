# Bug Report

### Describe the bug
When using multiple MDX extensions together, the last extension in the array is not being applied. It seems like the extension combination logic is skipping the final extension when merging them.

### Reproduction
```js
const extensions = [
  extensionA,
  extensionB,
  extensionC
];

// Only extensionA and extensionB are applied
// extensionC is ignored
const combined = combineExtensions(extensions);
```

### Expected behavior
All extensions in the array should be processed and merged together. The last extension should not be skipped.

### Additional context
This appears to affect any scenario where you're passing multiple extensions to be combined. If you only pass one or two extensions, you might not notice the issue, but with three or more extensions, the last one is consistently ignored.

---
Repository: /testbed
