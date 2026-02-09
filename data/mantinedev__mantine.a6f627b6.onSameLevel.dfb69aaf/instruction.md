# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in components that use scoped keydown handlers. When navigating between elements (like buttons in a toolbar or menu items), the arrow keys are not working as expected. It seems like the navigation logic is selecting elements from different scopes/containers instead of staying within the same parent container.

### Reproduction

```jsx
<Toolbar>
  <Button>First</Button>
  <Button>Second</Button>
  <Button>Third</Button>
</Toolbar>

<Toolbar>
  <Button>Another First</Button>
  <Button>Another Second</Button>
</Toolbar>
```

When I'm focused on "First" and press the arrow key to navigate, instead of moving to "Second" in the same toolbar, the focus jumps to buttons in the other toolbar. The scoped navigation doesn't seem to respect parent boundaries anymore.

### Expected behavior

Arrow key navigation should only move focus between elements within the same parent container/scope. When using arrow keys on a button in the first Toolbar, it should only cycle through buttons in that same Toolbar, not jump to buttons in other Toolbars.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox (happens in both)

---
Repository: /testbed
