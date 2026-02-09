# Bug Report

### Describe the bug

The Menu component's `onClose` callback is being triggered at the wrong time. Instead of firing when the menu is actually open and being closed, it's now firing when the menu is already closed (or when trying to close an already closed menu).

### Reproduction

```jsx
import { Menu } from '@mantine/core';

function Demo() {
  return (
    <Menu onClose={() => console.log('Menu closed')}>
      <Menu.Target>
        <button>Toggle menu</button>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Item>Item 1</Menu.Item>
        <Menu.Item>Item 2</Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
}
```

Steps to reproduce:
1. Open the menu by clicking the target button
2. Close the menu by clicking outside or pressing escape
3. The `onClose` callback doesn't fire
4. Try to close the menu again (even though it's already closed)
5. Now the `onClose` callback fires unexpectedly

### Expected behavior

The `onClose` callback should fire when the menu transitions from open to closed state, not when it's already closed.

Also noticing some weird behavior with the hover trigger mode - seems like the dropdown closing mechanism is using the wrong trigger condition.

---
Repository: /testbed
