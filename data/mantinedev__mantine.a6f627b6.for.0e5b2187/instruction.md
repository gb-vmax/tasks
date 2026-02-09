# Bug Report

### Describe the bug

When using the Combobox component with keyboard navigation, calling a method to select the first available option is selecting the wrong item. Instead of selecting the first non-disabled option, it appears to be selecting the last disabled option (if any exist), or returning no selection at all.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function Demo() {
  const combobox = useCombobox();
  
  return (
    <Combobox store={combobox}>
      <Combobox.Options>
        <Combobox.Option value="1">Option 1</Combobox.Option>
        <Combobox.Option value="2" disabled>Option 2 (disabled)</Combobox.Option>
        <Combobox.Option value="3">Option 3</Combobox.Option>
      </Combobox.Options>
    </Combobox>
  );
}

// When trying to select the first available option
// Expected: Option 1 should be selected
// Actual: Option 2 (the disabled one) gets selected instead
```

### Expected behavior

When navigating to the first option (e.g., pressing Home key or programmatically moving to the first option), the first **non-disabled** option should be selected. Disabled options should be skipped entirely.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
