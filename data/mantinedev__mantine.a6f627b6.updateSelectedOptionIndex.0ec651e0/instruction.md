# Bug Report

### Describe the bug

I'm experiencing an issue with `useVirtualizedCombobox` where the selected option index calculation seems incorrect when trying to manually update the selected option index. When the index goes beyond the bounds of the available options, the wrapping behavior produces unexpected results.

### Reproduction

```js
const combobox = useVirtualizedCombobox({
  // ... config
});

// Assume we have 5 options (indices 0-4)
combobox.updateSelectedOptionIndex(5); // Should wrap to first option
// Expected: selectedIndex = 0
// Actual: selectedIndex = 5 (out of bounds)

combobox.updateSelectedOptionIndex(-1); // Should wrap to last option
// Expected: selectedIndex = 4
// Actual: selectedIndex = -2 (incorrect calculation)
```

### Expected behavior

When `updateSelectedOptionIndex` is called with an index outside the valid range:
- Negative indices should wrap around to select options from the end
- Indices greater than or equal to the options length should wrap around to the beginning
- The selected index should always be within the valid range [0, options.length - 1]

### Additional context

This is causing keyboard navigation issues in virtualized comboboxes where cycling through options doesn't work as expected. When reaching the last option and pressing down, or reaching the first option and pressing up, the selection doesn't wrap correctly.

---
Repository: /testbed
