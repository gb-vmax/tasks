# Bug Report

### Describe the bug

When navigating backwards through Combobox options using keyboard (arrow up), the focus is jumping to disabled items instead of skipping them. The navigation should skip over disabled options and move to the next available enabled option, but it's doing the opposite.

### Reproduction

```jsx
import { Combobox, useCombobox } from '@mantine/core';

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
```

Steps to reproduce:
1. Open the combobox dropdown
2. Focus on "Option 3" 
3. Press arrow up key to navigate backwards
4. Focus moves to the disabled "Option 2" instead of skipping to "Option 1"

### Expected behavior

When pressing arrow up, the focus should skip over disabled options and land on the previous enabled option. In the example above, pressing arrow up from "Option 3" should move focus directly to "Option 1", not to the disabled "Option 2".

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
