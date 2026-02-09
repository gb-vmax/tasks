# Bug Report

### Describe the bug

When using `useVirtualizedCombobox`, the `updateSelectedOptionIndex` function doesn't work at all. It's currently a no-op function that doesn't update the selected option index when navigating through virtualized combobox options with keyboard controls.

### Reproduction

```tsx
import { useVirtualizedCombobox } from '@mantine/core';

const combobox = useVirtualizedCombobox({
  // ... config
});

// Try to update the selected option index
combobox.updateSelectedOptionIndex('down', 10, 0, (newIndex) => {
  console.log('New index:', newIndex);
});

// Nothing happens - the function is just an empty stub
```

### Expected behavior

The `updateSelectedOptionIndex` function should:
- Navigate through options based on direction ('up', 'down', or a specific index number)
- Handle boundary conditions (wrapping at start/end of list)
- Call the callback function with the new index
- Return the updated index value

Currently it just returns undefined and doesn't perform any navigation logic.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
