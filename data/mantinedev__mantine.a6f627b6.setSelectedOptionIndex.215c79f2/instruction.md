# Bug Report

### Describe the bug

I'm experiencing an issue with the virtualized combobox where selecting options beyond a certain index doesn't work properly. When I try to select an option at the last position in my list, the selection doesn't register and nothing happens.

### Reproduction

```js
const options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'];

const combobox = useVirtualizedCombobox({
  options,
  // ... other config
});

// Try to select the last option (index 4)
combobox.setSelectedOptionIndex(4);

// The option at index 4 is not selected
// Only options at indices 0-3 seem to work
```

### Expected behavior

When calling `setSelectedOptionIndex` with an index that corresponds to a valid option in the array, that option should be selected regardless of whether it's at the beginning, middle, or end of the list. The last option (index 4 in a 5-item array) should be selectable just like any other option.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
