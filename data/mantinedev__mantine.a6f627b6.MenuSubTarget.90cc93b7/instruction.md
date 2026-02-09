# Bug Report

### Describe the bug

When using nested menus (submenu), the `popupType` is incorrectly set to `"dialog"` instead of `"menu"` for the `MenuSubTarget` component. This affects accessibility as screen readers and assistive technologies rely on the correct ARIA role to understand the menu structure.

### Reproduction

```jsx
import { Menu } from '@mantine/core';

function Demo() {
  return (
    <Menu>
      <Menu.Target>
        <button>Main Menu</button>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Item>Item 1</Menu.Item>
        <Menu submenu>
          <Menu.SubTarget>
            <Menu.Item>Submenu trigger</Menu.Item>
          </Menu.SubTarget>
          <Menu.Dropdown>
            <Menu.Item>Submenu item</Menu.Item>
          </Menu.Dropdown>
        </Menu>
      </Menu.Dropdown>
    </Menu>
  );
}
```

When inspecting the DOM, the submenu target has the wrong ARIA attributes because `popupType` is set to `"dialog"` instead of `"menu"`.

### Expected behavior

The `MenuSubTarget` should have `popupType="menu"` to ensure proper accessibility semantics. Screen readers should announce it as a menu popup, not a dialog.

### System Info

- @mantine/core version: latest
- Browser: All browsers
- Impact: Accessibility compliance

---
Repository: /testbed
