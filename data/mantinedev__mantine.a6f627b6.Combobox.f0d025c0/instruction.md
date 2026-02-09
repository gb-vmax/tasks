# Bug Report

### Describe the bug

The Combobox dropdown is showing the opposite behavior - it appears when it should be closed and closes when it should be open. When clicking to open the dropdown, nothing happens, but the dropdown is actually visible when the component first renders (before any interaction).

### Reproduction

```jsx
import { Combobox, useCombobox } from '@mantine/core';

function Demo() {
  const combobox = useCombobox();

  return (
    <Combobox store={combobox}>
      <Combobox.Target>
        <button onClick={() => combobox.openDropdown()}>
          Open dropdown
        </button>
      </Combobox.Target>

      <Combobox.Dropdown>
        <Combobox.Option value="1">Option 1</Combobox.Option>
        <Combobox.Option value="2">Option 2</Combobox.Option>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

### Expected behavior

- Dropdown should be closed initially
- Clicking the button should open the dropdown
- The dropdown should close when clicking outside or selecting an option

### Actual behavior

- Dropdown is visible on initial render
- Clicking the button closes the dropdown instead of opening it
- The open/close behavior is completely inverted

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
