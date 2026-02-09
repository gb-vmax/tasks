# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in components that use the scoped keydown handler. When navigating backwards (e.g., using arrow up/left keys), the first element in the list is being skipped and cannot be focused.

### Reproduction

```js
// Setup a component with keyboard navigation
const items = [
  { label: 'Item 1', disabled: false },
  { label: 'Item 2', disabled: false },
  { label: 'Item 3', disabled: false }
];

// Steps:
// 1. Focus on Item 2 (index 1)
// 2. Press arrow up/left to navigate backwards
// 3. Expected: Item 1 should be focused
// 4. Actual: Navigation skips Item 1 and goes to Item 3 (when loop is enabled) or does nothing
```

### Expected behavior

When navigating backwards from any item, the previous enabled item should receive focus, including the first item (index 0) in the list. With loop enabled, navigating backwards from the first item should wrap to the last item.

### System Info
- @mantine/core version: latest
- Browser: All browsers

This seems to affect any component that relies on keyboard navigation with arrow keys, like menus, tabs, or custom navigable lists.

---
Repository: /testbed
