# Bug Report

### Describe the bug

When using the Combobox component with keyboard navigation, the "loop" behavior when pressing the up arrow key doesn't work as expected. Instead of properly cycling through all options when reaching the top, it seems to skip every other option and doesn't always land on the last enabled item.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function Demo() {
  const combobox = useCombobox({ loop: true });
  
  return (
    <Combobox store={combobox}>
      <Combobox.Target>
        <input />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Options>
          <Combobox.Option value="1">Option 1</Combobox.Option>
          <Combobox.Option value="2">Option 2</Combobox.Option>
          <Combobox.Option value="3">Option 3</Combobox.Option>
          <Combobox.Option value="4">Option 4</Combobox.Option>
          <Combobox.Option value="5">Option 5</Combobox.Option>
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

Steps to reproduce:
1. Open the combobox dropdown
2. Press the up arrow key when at the first option (or before selecting any option)
3. Notice that it doesn't go to the last option as expected, or skips options

### Expected behavior

When `loop: true` is enabled and the user presses the up arrow at the beginning of the list, it should wrap around to the last non-disabled option in the list. It should also iterate through all options, not skip any.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
