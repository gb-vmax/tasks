# Bug Report

### Describe the bug

I'm experiencing an issue with version ordering in the docs plugin. After updating, the versions array seems to be getting reordered unexpectedly - the first version is being moved to the end of the array instead of maintaining its original position.

### Reproduction

```js
const versions = [
  { version: 'current', label: 'Next' },
  { version: '2.0.0', label: '2.0.0' },
  { version: '1.0.0', label: '1.0.0' }
]

// After translation, the order becomes:
// [
//   { version: '2.0.0', label: '2.0.0' },
//   { version: '1.0.0', label: '1.0.0' },
//   { version: 'current', label: 'Next' }  // moved to end
// ]
```

### Expected behavior

The versions array should maintain its original order after translation. The first version should remain first, not be moved to the last position.

### Additional context

This affects the version dropdown ordering in the docs navigation. The current/latest version should appear first in the list, but it's now appearing at the end.

---
Repository: /testbed
