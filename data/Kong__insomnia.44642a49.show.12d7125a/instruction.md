# Bug Report

### Describe the bug

The SelectModal component is crashing when trying to display a modal with an empty options array. The modal should handle edge cases gracefully, but instead it throws an error when `options` is empty or when the provided `value` doesn't exist in the options list.

### Reproduction

```tsx
// This causes the modal to crash
selectModalRef.current?.show({
  title: 'Select an option',
  message: 'Please choose',
  options: [], // Empty options array
  value: null,
  onDone: (selectedValue) => console.log(selectedValue)
});

// This also causes issues
selectModalRef.current?.show({
  title: 'Select an option',
  message: 'Please choose',
  options: [
    { name: 'Option A', value: 'a' },
    { name: 'Option B', value: 'b' }
  ],
  value: 'invalid_value', // Value that doesn't exist in options
  onDone: (selectedValue) => console.log(selectedValue)
});
```

### Expected behavior

- When `options` is an empty array, the modal should handle it gracefully (maybe show a message or disable selection)
- When the provided `value` doesn't match any option, it should default to the first available option or handle it appropriately instead of breaking

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
