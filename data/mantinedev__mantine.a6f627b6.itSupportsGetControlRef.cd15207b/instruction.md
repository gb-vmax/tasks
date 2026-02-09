# Bug Report

### Describe the bug

The `__getControlRef` callback is being invoked incorrectly in date picker components. Instead of being called once per control with the expected arguments, it appears the callback signature and invocation pattern has changed.

### Reproduction

```tsx
const getControlRef = jest.fn();

<DatePicker __getControlRef={getControlRef} />

// Expected: getControlRef to be called multiple times (once per control)
// Actual: getControlRef is called differently than expected
```

When using the `__getControlRef` prop on date components, the callback function receives arguments in an unexpected format. The number of times the callback is invoked and the structure of the arguments passed don't match what was previously working.

### Expected behavior

The `__getControlRef` callback should be called once for each control element in the component (e.g., for each day button in a calendar), with each call receiving:
- Row index (number)
- Column index (number)  
- The control element reference (HTMLButtonElement)

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
