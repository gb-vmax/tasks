# Bug Report

### Describe the bug

The `useDisclosure` hook is calling the wrong callback function when opening. When I call the `open()` function returned by `useDisclosure`, it triggers the `onClose` callback instead of the `onOpen` callback.

### Reproduction

```js
const [opened, { open, close }] = useDisclosure(false, {
  onOpen: () => console.log('opened'),
  onClose: () => console.log('closed'),
});

// Clicking this button logs "closed" instead of "opened"
<button onClick={open}>Open Modal</button>
```

### Expected behavior

When calling `open()`, the `onOpen` callback should be triggered, not `onClose`. Currently it's backwards - opening triggers the close callback.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
