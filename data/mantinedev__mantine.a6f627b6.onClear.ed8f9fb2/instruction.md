# Bug Report

### Describe the bug

The `ComboboxClearButton` component is not working properly - it appears to be completely broken and doesn't render anything. When trying to use it with a Combobox, the clear button just doesn't show up at all, even when there's a value selected.

### Reproduction

```tsx
import { Combobox, ComboboxClearButton } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('test');
  
  return (
    <Combobox value={value} onChange={setValue}>
      <Combobox.Target>
        <Input value={value} onChange={(e) => setValue(e.target.value)} />
      </Combobox.Target>
      <ComboboxClearButton onClear={() => setValue('')} />
    </Combobox>
  );
}
```

### Expected behavior

The clear button should appear when there's a value in the input field and clicking it should clear the value. Instead, nothing renders at all.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems like it might have been introduced in a recent update? The component was working fine before.

---
Repository: /testbed
