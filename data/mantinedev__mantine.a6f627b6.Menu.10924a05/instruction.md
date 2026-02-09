# Bug Report

### Describe the bug

The `onOpen` and `onClose` callbacks in the Menu component are firing at the wrong times. When opening the menu, `onClose` gets called instead of `onOpen`, and when closing the menu, `onOpen` gets called instead of `onClose`. This is causing unexpected behavior in my application where I'm trying to track menu state changes.

### Reproduction

```jsx
import { Menu, Button } from '@mantine/core';

function MyComponent() {
  return (
    <Menu
      onOpen={() => console.log('Menu opened')}
      onClose={() => console.log('Menu closed')}
    >
      <Menu.Target>
        <Button>Toggle menu</Button>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Item>Item 1</Menu.Item>
        <Menu.Item>Item 2</Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
}
```

### Expected behavior

- When clicking the button to open the menu, the console should log "Menu opened"
- When closing the menu (clicking outside or on an item), the console should log "Menu closed"

### Actual behavior

- When opening the menu, "Menu closed" is logged
- When closing the menu, "Menu opened" is logged

The callbacks are being invoked in reverse - `onClose` fires when the menu opens and `onOpen` fires when it closes.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
