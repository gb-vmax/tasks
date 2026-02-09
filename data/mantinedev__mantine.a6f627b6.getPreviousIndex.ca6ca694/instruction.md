# Bug Report

### Describe the bug

Keyboard navigation isn't working correctly when trying to navigate backwards through a list of elements. When pressing the up/left arrow key to move to the previous element, the first element (index 0) in the list is being skipped and cannot be focused.

### Reproduction

```js
// Setup a list of focusable elements where the first one is enabled
const elements = [
  { disabled: false }, // index 0 - should be focusable
  { disabled: false }, // index 1
  { disabled: false }  // index 2
];

// Start at index 1 and try to navigate backwards
// Expected: should move to index 0
// Actual: skips index 0 and doesn't focus anything
```

### Steps to reproduce:
1. Create a component with multiple focusable elements (buttons, inputs, etc.)
2. Focus on the second element
3. Press the arrow key to navigate backwards to the first element
4. The first element is skipped and cannot be reached via keyboard navigation

### Expected behavior

When navigating backwards through elements, all enabled elements including the first one (index 0) should be focusable. The keyboard navigation should allow users to reach every non-disabled element in the list.

### Additional context

This seems to affect any component using scoped keydown handlers for keyboard navigation. The issue only occurs when navigating backwards - forward navigation works as expected.

---
Repository: /testbed
