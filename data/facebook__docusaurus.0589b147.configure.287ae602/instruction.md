# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX configuration system where passing an empty array as an extension causes unexpected behavior. The configuration seems to skip the first valid extension in the array when processing.

### Reproduction

```js
const extensions = [
  { /* first extension config */ },
  { /* second extension config */ },
  []  // empty array
]

configure(combined, extensions)
```

When the extensions array contains mixed valid objects and empty arrays, the first extension in the list doesn't get processed correctly. It appears that the iteration starts at the wrong index.

### Expected behavior

All valid extension configurations should be processed regardless of whether empty arrays are present in the extensions list. The first extension should not be skipped during iteration.

### Additional context

This seems to affect how MDX processes configuration extensions when they're passed as nested arrays. The issue manifests when you have a configuration setup with multiple extensions where some might be conditionally empty.

---
Repository: /testbed
