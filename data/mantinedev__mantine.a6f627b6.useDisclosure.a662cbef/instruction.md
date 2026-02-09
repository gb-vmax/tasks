# Bug Report

### Describe the bug

When using `useDisclosure` hook with `onOpen` or `onClose` callbacks, the callbacks don't get updated when they change. If you pass new callback functions through the options, the hook still uses the old/initial callbacks.

### Reproduction

```jsx
const [count, setCount] = useState(0);

const [opened, { open, close }] = useDisclosure(false, {
  onOpen: () => console.log('Open callback - count:', count),
  onClose: () => console.log('Close callback - count:', count)
});

// Later, when count changes to 1, 2, 3, etc.
// The callbacks still log count: 0
```

The callbacks are captured at the initial render and never update even when the `count` dependency changes.

### Expected behavior

The `onOpen` and `onClose` callbacks should use the latest values from the component scope. When dependencies of these callbacks change, the hook should use the updated callback functions.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
