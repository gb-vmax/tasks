# Bug Report

### Combobox keyboard navigation broken - Cannot navigate to first enabled option

I'm experiencing an issue with the Combobox component where keyboard navigation completely stops working. When I try to use arrow keys to navigate through options, nothing happens and the focus doesn't move to any option.

### Reproduction
```jsx
import { Combobox } from '@mantine/core';

function Demo() {
  return (
    <Combobox>
      <Combobox.Target>
        <input />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Option value="1">Option 1</Combobox.Option>
        <Combobox.Option value="2">Option 2</Combobox.Option>
        <Combobox.Option value="3">Option 3</Combobox.Option>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

Steps to reproduce:
1. Open the combobox dropdown
2. Try to use arrow down key to navigate to the first option
3. Nothing happens - no option gets focused

This also affects cases where some options are disabled and I need to skip to the first enabled option.

### Expected behavior
Pressing arrow down should focus the first available (non-disabled) option in the list.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
