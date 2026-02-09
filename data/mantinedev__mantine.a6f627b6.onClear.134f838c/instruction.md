# Bug Report

### Describe the bug

The `ComboboxClearButton` component appears to be completely broken after a recent change. The code structure looks corrupted with duplicate function definitions and the component doesn't render properly.

### Reproduction

```tsx
import { Combobox } from '@mantine/core';

function MyComponent() {
  return (
    <Combobox>
      <Combobox.Target>
        <input />
      </Combobox.Target>
      <Combobox.ClearButton onClear={() => console.log('cleared')} />
    </Combobox>
  );
}
```

### Expected behavior

The clear button should render and be clickable when there's a value to clear. Instead, the component fails to render or throws errors during compilation.

### System Info

- @mantine/core version: latest
- React version: 18.x

The component definition seems to have syntax errors with overlapping code blocks. It looks like there might have been a bad merge or incomplete refactoring.

---
Repository: /testbed
