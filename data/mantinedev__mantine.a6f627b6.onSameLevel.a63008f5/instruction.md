# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in components that use scoped keydown handlers. When navigating between focusable elements (like buttons) using arrow keys, the focus doesn't move to sibling elements as expected. It seems like the handler is not correctly identifying elements that are on the same level in the DOM hierarchy.

### Reproduction

```jsx
<div data-scope="navigation">
  <button>Button 1</button>
  <button>Button 2</button>
  <button>Button 3</button>
</div>
```

Steps to reproduce:
1. Create a component with multiple buttons wrapped in a container with a scope selector
2. Focus on the first button
3. Press arrow keys to navigate to sibling buttons
4. The focus doesn't move to the next/previous button

### Expected behavior

When pressing arrow keys, focus should move between sibling elements that share the same parent scope. The scoped keydown handler should correctly identify elements on the same level and allow navigation between them.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox/Safari (happens on all)

---
Repository: /testbed
