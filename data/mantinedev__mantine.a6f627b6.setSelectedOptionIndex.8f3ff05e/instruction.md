# Bug Report

### Describe the bug

I'm experiencing an issue with `useVirtualizedCombobox` where the `setSelectedOptionIndex` function doesn't properly handle invalid index values. When passing an index that's out of bounds, the function doesn't prevent the update and can cause unexpected behavior.

### Reproduction

```js
const combobox = useVirtualizedCombobox({
  options: ['Option 1', 'Option 2', 'Option 3'],
  // ... other config
});

// This should not work but causes issues
combobox.setSelectedOptionIndex(10); // index beyond array length

// Also problematic with negative values
combobox.setSelectedOptionIndex(-5);
```

### Expected behavior

The function should validate the index before attempting to update the selected option. Invalid indices (negative numbers or values exceeding the options array length) should be ignored or handled gracefully without breaking the component state.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
