# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in components that use scoped keydown handlers. When trying to navigate between buttons/elements using arrow keys, the focus is jumping to elements in different parent containers instead of staying within the same level/scope.

### Reproduction

```jsx
<div data-scope="menu-1">
  <button>Item 1</button>
  <button>Item 2</button>
  <button>Item 3</button>
</div>

<div data-scope="menu-2">
  <button>Item A</button>
  <button>Item B</button>
</div>
```

When I press arrow keys while focused on "Item 1", the focus moves to "Item A" in the second menu instead of staying within the first menu and moving to "Item 2".

### Expected behavior

Arrow key navigation should only move focus between elements that share the same parent scope. Focus should not jump across different parent containers.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: macOS

---
Repository: /testbed
