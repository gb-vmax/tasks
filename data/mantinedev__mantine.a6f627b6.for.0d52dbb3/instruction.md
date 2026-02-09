# Bug Report

### Describe the bug

When using the Combobox component with keyboard navigation, pressing the down arrow key or trying to navigate to the first available option skips the first item in the list. The focus always starts from the second option instead of the first one.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function Demo() {
  const combobox = useCombobox();
  
  return (
    <Combobox store={combobox}>
      <Combobox.Target>
        <input />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Options>
          <Combobox.Option value="1">First option</Combobox.Option>
          <Combobox.Option value="2">Second option</Combobox.Option>
          <Combobox.Option value="3">Third option</Combobox.Option>
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

Steps to reproduce:
1. Create a Combobox with multiple options
2. Open the dropdown
3. Press the down arrow key or trigger keyboard navigation
4. Notice that the first option is skipped and focus goes directly to the second option

### Expected behavior

The first option should be focused when navigating with keyboard for the first time. All options should be accessible via keyboard navigation starting from index 0.

---
Repository: /testbed
