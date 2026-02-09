# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in components that use scoped keydown handlers. When navigating backwards (e.g., using arrow keys or similar), the navigation is skipping elements instead of moving to the previous enabled item.

### Reproduction

```js
// Setup a component with multiple focusable elements
const elements = [
  { disabled: false },
  { disabled: false },
  { disabled: false },
  { disabled: false }
]

// When currently focused on index 3 and pressing key to go backwards
// Expected: Should move to index 2
// Actual: Skips index 2 and jumps to index 1 (or further)
```

The problem seems to be that when navigating backwards through a list of elements, it's jumping over valid items instead of selecting the immediately previous non-disabled element.

### Expected behavior

When navigating backwards with keyboard controls:
- Should move to the immediately previous non-disabled element
- Should respect the loop parameter when reaching the beginning
- Should not skip over valid elements

### Additional context

This affects keyboard navigation in components like tabs, menu items, and other keyboard-accessible UI elements. The forward navigation seems to work fine, but backward navigation is problematic.

---
Repository: /testbed
