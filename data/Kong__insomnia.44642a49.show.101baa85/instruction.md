# Bug Report

### Describe the bug

The SelectModal component is crashing when trying to show the modal with a `null` or `undefined` value. After a recent update, the modal fails to open and throws an error when the initial value doesn't match any of the provided options.

### Reproduction

```js
const selectModal = useRef();

// This causes the modal to fail
selectModal.current?.show({
  title: 'Select an option',
  message: 'Please choose',
  options: [
    { name: 'Option 1', value: 'opt1' },
    { name: 'Option 2', value: 'opt2' }
  ],
  value: null, // or undefined, or a value that doesn't exist in options
  onDone: (value) => console.log(value)
});
```

### Expected behavior

The modal should open successfully and either:
- Default to the first option when value is null/undefined
- Handle invalid values gracefully by selecting a default

### System Info

- Insomnia version: latest
- OS: macOS

This was working fine before and the modal would just default to the first option. Now it seems to break completely when the value doesn't match.

---
Repository: /testbed
