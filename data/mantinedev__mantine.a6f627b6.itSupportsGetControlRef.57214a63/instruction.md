# Bug Report

### Describe the bug

The `__getControlRef` callback is being called with incorrect parameters. The first argument is expected to be a number (index), but it's receiving a string instead. Additionally, the callback is being invoked more times than expected based on the number of controls.

### Reproduction

```tsx
const getControlRefSpy = jest.fn();

<DatePicker 
  __getControlRef={getControlRefSpy}
  // ... other props
/>

// The callback receives wrong parameter types:
// Expected: getControlRef(rowIndex: number, colIndex: number, element: HTMLButtonElement)
// Actual: getControlRef(someString, colIndex: number, element: HTMLButtonElement)
```

### Expected behavior

The `__getControlRef` callback should:
1. Be called exactly `numberOfControls` times (once per control)
2. Receive a numeric row index as the first parameter, not a string

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
