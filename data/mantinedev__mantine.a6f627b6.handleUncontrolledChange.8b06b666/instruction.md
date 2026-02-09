# Bug Report

### Describe the bug

I'm experiencing an issue with the `useUncontrolled` hook where the `onChange` callback receives incorrect arguments when used in uncontrolled mode. The callback is receiving an array instead of the individual payload arguments.

### Reproduction

```tsx
const [value, handleChange] = useUncontrolled({
  defaultValue: 'initial',
  onChange: (val, arg1, arg2) => {
    console.log('Value:', val);
    console.log('Arg1:', arg1);  // Expected: actual arg1, Getting: [arg1, arg2]
    console.log('Arg2:', arg2);  // Expected: actual arg2, Getting: undefined
  }
});

// When calling the handler with multiple arguments
handleChange('newValue', 'firstArg', 'secondArg');
```

### Expected behavior

When `onChange` is called with additional payload arguments, they should be spread correctly to the callback function. Each argument should be passed individually, not wrapped in an array.

For example:
- `onChange(val, arg1, arg2)` should receive three separate arguments
- Currently it seems to receive `onChange(val, [arg1, arg2])` instead

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
