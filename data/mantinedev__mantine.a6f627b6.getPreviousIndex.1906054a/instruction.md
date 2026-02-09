# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in components that use scoped keydown handlers. When navigating backwards through a list of elements (e.g., using arrow keys), the first element (index 0) is being skipped and can't be focused.

### Reproduction

```js
// Setup: Create a component with multiple focusable elements
const elements = [
  { disabled: false }, // index 0 - THIS ELEMENT GETS SKIPPED
  { disabled: false }, // index 1
  { disabled: false }, // index 2
  { disabled: false }  // index 3
];

// Current behavior:
// 1. Start at index 2
// 2. Press arrow key to navigate backwards
// 3. Focus moves to index 1
// 4. Press arrow key again
// 5. Focus jumps to index 3 (with loop enabled) or stays at index 1
// 6. Element at index 0 is never reachable
```

### Expected behavior

When navigating backwards through focusable elements, the element at index 0 should be included in the navigation cycle. It should be possible to reach and focus the first element in the list.

### Additional context

This seems to affect any component that uses keyboard navigation with arrow keys, particularly when:
- Loop navigation is enabled
- Trying to navigate backwards from any position
- The first element in the list is not disabled

The first element appears to be completely excluded from the backward navigation cycle, which breaks the expected keyboard navigation UX.

---
Repository: /testbed
