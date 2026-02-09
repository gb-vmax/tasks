# Bug Report

### Describe the bug

When using a controlled Combobox with a custom store, the dropdown doesn't close properly when clicking outside or pressing Escape. The dropdown remains open even though the `onClose` callback is fired.

### Reproduction

```jsx
import { Combobox, useCombobox } from '@mantine/core';

function MyComponent() {
  const store = useCombobox({
    onDropdownClose: () => console.log('Dropdown closed'),
  });

  return (
    <Combobox store={store}>
      <Combobox.Target>
        <input />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Option value="1">Option 1</Combobox.Option>
        <Combobox.Option value="2">Option 2</Combobox.Option>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

Steps to reproduce:
1. Create a Combobox with a controlled store
2. Open the dropdown by clicking the input
3. Try to close it by clicking outside or pressing Escape
4. The dropdown stays open (though the onClose callback fires)

### Expected behavior

The dropdown should close when clicking outside or pressing Escape, just like it does when using an uncontrolled Combobox (without passing a custom store).

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
