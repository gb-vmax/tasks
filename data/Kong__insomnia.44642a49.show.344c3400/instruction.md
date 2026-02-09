# Bug Report

### Describe the bug

The SelectModal component is not displaying correctly when provided with a valid value that exists in the options array. After a recent update, the modal seems to be ignoring the `value` prop and defaulting to the first option instead, even when a specific value is explicitly provided.

### Reproduction

```js
const modalRef = useRef();

// Show modal with a specific value selected
modalRef.current?.show({
  title: 'Select an option',
  message: 'Choose one',
  options: [
    { name: 'Option 1', value: 'opt1' },
    { name: 'Option 2', value: 'opt2' },
    { name: 'Option 3', value: 'opt3' }
  ],
  value: 'opt2',  // Should select Option 2
  onDone: (selected) => console.log(selected)
});
```

### Expected behavior

The modal should open with "Option 2" selected since `value: 'opt2'` is provided and exists in the options array. Instead, it appears to always select the first option regardless of what value is passed.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
