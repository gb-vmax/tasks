# Bug Report

### Describe the bug

The `Menu` component's `onClose` callback is being triggered at the wrong time. When I try to close an already closed menu, the `onClose` handler fires, but it should only fire when the menu is actually open and being closed.

### Reproduction

```jsx
import { Menu, Button } from '@mantine/core';

function Demo() {
  const handleClose = () => {
    console.log('Menu closed!');
  };

  return (
    <Menu onClose={handleClose}>
      <Menu.Target>
        <Button>Toggle menu</Button>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Item>Item 1</Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
}
```

Steps to reproduce:
1. Render a Menu component with an `onClose` callback
2. Keep the menu closed (don't open it)
3. Call the close function programmatically or trigger a close action
4. The `onClose` callback fires even though the menu was never open

### Expected behavior

The `onClose` callback should only be invoked when the menu transitions from open to closed state, not when it's already closed.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
