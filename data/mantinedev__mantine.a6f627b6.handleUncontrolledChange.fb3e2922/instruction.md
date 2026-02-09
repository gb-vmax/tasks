# Bug Report

### Describe the bug

When using `useUncontrolled` hook with an `onChange` callback, the callback is being invoked with incorrect arguments. The second parameter passed to `onChange` is not being spread correctly - it receives only the first element of the payload array instead of all the additional arguments.

### Reproduction

```tsx
const [value, setValue] = useUncontrolled({
  value: controlledValue,
  defaultValue: 'initial',
  onChange: (val, ...rest) => {
    console.log('Value:', val);
    console.log('Additional args:', rest);
    // Expected: rest should contain all additional arguments
    // Actual: rest only contains the first additional argument
  }
});

// When calling with multiple payload arguments:
setValue('newValue', 'arg1', 'arg2', 'arg3');
// onChange receives: ('newValue', 'arg1') instead of ('newValue', 'arg1', 'arg2', 'arg3')
```

### Expected behavior

The `onChange` callback should receive all the additional arguments that were passed to the setter function, not just the first one. If I call `setValue(newVal, extra1, extra2)`, the `onChange` should be invoked with `(newVal, extra1, extra2)`.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
