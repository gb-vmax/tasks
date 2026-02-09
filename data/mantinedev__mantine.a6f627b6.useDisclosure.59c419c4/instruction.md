# Bug Report

### Describe the bug

The `useDisclosure` hook's `close()` function is not working as expected. When I call `close()`, the `onClose` callback is being triggered even when the disclosure is already closed, and the state doesn't seem to update properly.

### Reproduction

```jsx
const [opened, { close }] = useDisclosure(true, {
  onClose: () => console.log('onClose called')
});

// Call close when already opened
close(); // Expected: state becomes false, onClose is called
// Actual: onClose is NOT called, state doesn't change

// Call close again when already closed
close(); // Expected: nothing happens
// Actual: onClose is called incorrectly
```

### Expected behavior

When calling `close()`:
- If the disclosure is currently open (`opened === true`), it should set the state to `false` and trigger the `onClose` callback
- If the disclosure is already closed (`opened === false`), it should do nothing and not trigger the callback

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
