# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in the Combobox component. When pressing the up arrow key to navigate through options, it's skipping every other item instead of moving to the previous option.

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
2. Use arrow down to select "Option 5"
3. Press arrow up key
4. Notice it jumps to "Option 3" instead of "Option 4"
5. Press arrow up again
6. It jumps to "Option 1" instead of "Option 2"

### Expected behavior

When pressing the up arrow key, the focus should move to the immediately previous option in the list, not skip options.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
