# Bug Report

### Describe the bug

When navigating backwards through Combobox options using keyboard controls, the current item is being skipped and navigation jumps to the item before it. This makes it impossible to select certain items when navigating upwards.

### Reproduction

```tsx
import { Combobox } from '@mantine/core';

function Demo() {
  const combobox = useCombobox();
  
  return (
    <Combobox store={combobox}>
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
2. Navigate down to "Option 3" using arrow keys
3. Press the up arrow key
4. Expected: "Option 2" should be highlighted
5. Actual: "Option 3" stays highlighted (the current item is skipped)

### Expected behavior

When pressing the up arrow key, the selection should move to the previous option in the list. The current item should not be skipped during backwards navigation.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
