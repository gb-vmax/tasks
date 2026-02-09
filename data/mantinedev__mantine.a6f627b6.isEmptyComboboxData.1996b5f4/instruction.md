# Bug Report

### Describe the bug

The `Combobox` component is incorrectly treating non-empty data as empty in certain scenarios. When providing data with a single option or when using grouped options, the dropdown behaves as if no data is available.

### Reproduction

```js
// Case 1: Single option is treated as empty
const singleOption = [
  { value: 'option1', label: 'Option 1' }
];

<Combobox data={singleOption} />
// Dropdown shows empty state instead of displaying the option

// Case 2: Grouped options are treated as empty
const groupedOptions = [
  { group: 'Group 1', items: [
    { value: 'item1', label: 'Item 1' },
    { value: 'item2', label: 'Item 2' }
  ]}
];

<Combobox data={groupedOptions} />
// Dropdown shows empty state even though items exist
```

### Expected behavior

- A single option should be displayed in the dropdown, not treated as empty data
- Grouped options should be displayed correctly and not trigger the empty state

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
