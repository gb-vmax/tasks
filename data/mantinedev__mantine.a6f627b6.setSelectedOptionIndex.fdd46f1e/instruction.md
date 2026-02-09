# Bug Report

### Describe the bug

I'm encountering an issue with `useVirtualizedCombobox` where the `setSelectedOptionIndex` function doesn't work properly. When trying to set the selected option index, nothing happens and the state doesn't update as expected.

### Reproduction

```js
const combobox = useVirtualizedCombobox({
  // ... other options
});

const options = ['Option 1', 'Option 2', 'Option 3'];

// Trying to set the selected index
combobox.setSelectedOptionIndex(1, options, (selected) => {
  console.log('Selected:', selected);
});

// Expected: selectedOptionIndex should be 1
// Actual: nothing happens, the function is a no-op
```

### Expected behavior

The `setSelectedOptionIndex` function should:
1. Update the selected option index in the store
2. Handle out-of-bounds indices appropriately
3. Call the callback function with the selected option if provided

Currently it's just an empty function that does nothing.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
