# Bug Report

### Describe the bug

When using grouped options in Combobox, duplicate values across different groups are incorrectly flagged as duplicates even though they should be allowed within separate option groups.

### Reproduction

```tsx
const options = [
  {
    group: 'Group 1',
    items: [
      { value: 'option-1', label: 'Option 1' },
      { value: 'option-2', label: 'Option 2' },
    ],
  },
  {
    group: 'Group 2',
    items: [
      { value: 'option-1', label: 'Different Option 1' },
      { value: 'option-3', label: 'Option 3' },
    ],
  },
];

// This throws an error about duplicate "option-1" 
// even though they're in different groups
<Combobox data={options} />
```

### Expected behavior

Options with the same value should be allowed to exist in different option groups without triggering a duplicate error. The validation should only check for duplicates within the same group, not across all groups.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
