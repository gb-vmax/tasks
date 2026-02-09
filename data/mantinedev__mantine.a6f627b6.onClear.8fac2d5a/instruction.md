# Bug Report

### Describe the bug

After a recent update, the `ComboboxClearButton` component appears to have duplicate function implementations. The component seems to have been refactored but the old implementation wasn't removed, causing the component to not render or function correctly.

### Reproduction

```tsx
import { Combobox } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('test');
  
  return (
    <Combobox>
      <Combobox.Target>
        <TextInput 
          value={value} 
          onChange={(e) => setValue(e.currentTarget.value)}
        />
      </Combobox.Target>
      <Combobox.ClearButton onClear={() => setValue('')} />
    </Combobox>
  );
}
```

### Expected behavior

The clear button should render and work properly when clicked. Instead, the component doesn't seem to render at all or throws an error due to malformed code structure.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

The issue appears to be in the `ComboboxClearButton.tsx` file where there seem to be two function definitions overlapping each other. The new implementation is added but the old one wasn't properly removed.

---
Repository: /testbed
