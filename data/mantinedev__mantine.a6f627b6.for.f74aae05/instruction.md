# Bug Report

### Describe the bug

When using the Combobox component, keyboard navigation doesn't work correctly. The first item in the dropdown is being skipped when navigating with arrow keys or when the combobox opens.

### Reproduction

```jsx
import { Combobox, useCombobox } from '@mantine/core';

function Demo() {
  const combobox = useCombobox();
  
  return (
    <Combobox store={combobox}>
      <Combobox.Target>
        <input />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Options>
          <Combobox.Option value="1">First Option</Combobox.Option>
          <Combobox.Option value="2">Second Option</Combobox.Option>
          <Combobox.Option value="3">Third Option</Combobox.Option>
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

Steps to reproduce:
1. Open the combobox dropdown
2. Notice that focus goes to the second item instead of the first
3. Try pressing the down arrow key - it skips the first option

### Expected behavior

The first option in the list should be focused/selected when the dropdown opens or when navigating from the top. Keyboard navigation should include all enabled options starting from the first one.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
