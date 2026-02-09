# Bug Report

### Describe the bug

Keyboard navigation is completely broken in components that use scoped keydown handlers. When pressing arrow keys or other navigation keys, the focus doesn't move between elements as expected. It seems like the handler is unable to determine if elements are on the same level in the DOM hierarchy.

### Reproduction

```jsx
import { Menu } from '@mantine/core';

function Demo() {
  return (
    <Menu>
      <Menu.Target>
        <Button>Toggle menu</Button>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Item>Item 1</Menu.Item>
        <Menu.Item>Item 2</Menu.Item>
        <Menu.Item>Item 3</Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
}
```

Steps to reproduce:
1. Open the menu
2. Try to navigate between menu items using arrow keys
3. Focus doesn't move at all, stays on the first item

This also affects other components like Select, Combobox, etc. that rely on keyboard navigation within a scoped container.

### Expected behavior

Arrow keys should move focus between sibling elements within the same parent scope. The navigation should work smoothly between items at the same DOM level.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
