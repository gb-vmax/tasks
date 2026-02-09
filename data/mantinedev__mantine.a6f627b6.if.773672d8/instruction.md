# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with the `useLongPress` hook. The `onFinish` callback is being triggered at the wrong time - it seems to fire when the long press is NOT active instead of when it completes successfully.

### Reproduction

```jsx
const longPressHandlers = useLongPress(
  () => console.log('Long press detected'),
  {
    onFinish: () => console.log('Long press finished'),
    onCancel: () => console.log('Long press cancelled'),
    threshold: 500,
  }
);

// Apply handlers to a button
<button {...longPressHandlers}>Press and hold me</button>
```

Steps to reproduce:
1. Press and hold the button for less than the threshold duration
2. Release the button
3. The `onFinish` callback fires even though the long press was never activated

### Expected behavior

The `onFinish` callback should only be called when a successful long press completes (i.e., when the user holds for the full threshold duration and then releases). If the user releases before the threshold, `onCancel` should fire instead.

Currently it seems like the logic is inverted - `onFinish` fires when the long press is not active, which doesn't make sense.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
