# Bug Report

### Describe the bug

When using the `Select` component with `selectFirstOptionOnDropdownOpen` prop, the behavior is inverted. Setting `selectFirstOptionOnDropdownOpen={true}` doesn't select the first option, and setting it to `false` (or leaving it unset) causes the first option to be selected instead.

### Reproduction

```jsx
import { Select } from '@mantine/core';

function Demo() {
  return (
    <Select
      data={['Option 1', 'Option 2', 'Option 3']}
      selectFirstOptionOnDropdownOpen={true}
      label="Select with first option auto-select"
    />
  );
}
```

Steps to reproduce:
1. Create a Select component with `selectFirstOptionOnDropdownOpen={true}`
2. Click to open the dropdown
3. Notice that the first option is NOT selected/highlighted

When you set `selectFirstOptionOnDropdownOpen={false}` or omit the prop entirely, the first option gets selected, which is the opposite of what should happen.

### Expected behavior

When `selectFirstOptionOnDropdownOpen` is set to `true`, the first option should be automatically selected when the dropdown opens. When it's `false` or undefined, it should maintain the current active option or have no selection.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
