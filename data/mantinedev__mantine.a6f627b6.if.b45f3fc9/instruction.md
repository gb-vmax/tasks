# Bug Report

### Describe the bug

When using keyboard navigation in a Combobox with `loop` enabled, pressing the up arrow key doesn't properly loop back to the last item when you're at the first item. Instead of going to the bottom of the list, it seems to get stuck or behave unexpectedly.

### Reproduction

```jsx
import { Combobox, useCombobox } from '@mantine/core';

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
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

Steps to reproduce:
1. Open the combobox dropdown
2. Navigate to the first option
3. Press the up arrow key
4. Expected: should loop to the last option (Option 4)
5. Actual: navigation doesn't work as expected

### Expected behavior

With `loop: true`, pressing up arrow on the first item should move focus to the last enabled item in the list, creating a circular navigation pattern.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
