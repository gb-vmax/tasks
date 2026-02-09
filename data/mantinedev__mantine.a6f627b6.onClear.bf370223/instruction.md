# Bug Report

### Describe the bug

The ComboboxClearButton component is broken after a recent change. When trying to use it, the component doesn't render properly and the clear functionality is completely broken.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function MyComponent() {
  const [value, setValue] = useState('test');
  
  return (
    <Combobox>
      <Combobox.Target>
        <Input value={value} onChange={(e) => setValue(e.target.value)} />
      </Combobox.Target>
      <Combobox.ClearButton onClear={() => setValue('')} />
    </Combobox>
  );
}
```

The clear button doesn't show up at all and the console shows errors about the component structure.

### Expected behavior

The ComboboxClearButton should render correctly and call the `onClear` callback when clicked. It should work with the standard Combobox component without any issues.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
