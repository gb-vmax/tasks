# Bug Report

### Describe the bug

The `ComboboxClearButton` component is completely broken after a recent change. It looks like there was a merge conflict or accidental duplication in the code - the component now has two separate implementations stacked on top of each other, which causes it to not render properly at all.

### Reproduction

```tsx
import { Combobox } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  
  return (
    <Combobox>
      <Combobox.Target>
        <TextInput 
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
      </Combobox.Target>
      <Combobox.ClearButton onClear={() => setValue('')} />
    </Combobox>
  );
}
```

### Expected behavior

The clear button should render and work as it did before. Instead, the component appears to have duplicate/conflicting code that prevents it from functioning.

### System Info

- @mantine/core version: latest
- React version: 18.x

This looks like it might have been introduced during a merge or refactoring. The component file has what appears to be two different implementations overlapping each other.

---
Repository: /testbed
