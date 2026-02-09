# Bug Report

### Describe the bug

After a recent update, the `useVirtualizedCombobox` hook appears to be completely non-functional. When trying to use it in my component, I'm getting errors that the function doesn't exist or is undefined.

### Reproduction

```tsx
import { useVirtualizedCombobox } from '@mantine/core';

function MyComponent() {
  const combobox = useVirtualizedCombobox({
    totalOptionsCount: 10,
    getOptionId: (index) => `option-${index}`,
    selectedOptionIndex: 0,
    setSelectedOptionIndex: () => {},
    onSelectedOptionSubmit: () => {},
  });

  // combobox is undefined
  return <div>...</div>;
}
```

### Expected behavior

The `useVirtualizedCombobox` hook should be properly exported and functional, returning a ComboboxStore object with methods like `openDropdown`, `closeDropdown`, `selectOption`, etc.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

The hook was working fine before, but now it seems like the entire implementation is missing or incomplete. This is blocking our virtualized select/combobox components from working.

---
Repository: /testbed
