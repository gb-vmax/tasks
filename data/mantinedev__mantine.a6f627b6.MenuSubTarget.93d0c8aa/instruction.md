# Bug Report

### Describe the bug

I'm having an issue with `Menu.Sub.Target` where the submenu is not working properly. The submenu doesn't open when hovering over the target element, and keyboard navigation seems broken.

### Reproduction

```jsx
<Menu>
  <Menu.Target>
    <Button>Main Menu</Button>
  </Menu.Target>
  <Menu.Dropdown>
    <Menu.Item>Item 1</Menu.Item>
    <Menu.Sub>
      <Menu.Sub.Target>
        <Menu.Item>Has Submenu</Menu.Item>
      </Menu.Sub.Target>
      <Menu.Sub.Dropdown>
        <Menu.Item>Submenu Item 1</Menu.Item>
        <Menu.Item>Submenu Item 2</Menu.Item>
      </Menu.Sub.Dropdown>
    </Menu.Sub>
  </Menu.Dropdown>
</Menu>
```

### Expected behavior

The submenu should open on hover and be accessible via keyboard navigation. The submenu should behave like a proper menu with correct ARIA attributes.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
