# Bug Report

### Describe the bug

The NumberInput component is not allowing increments when the input field is empty. When I try to use the increment button (or arrow up) on an empty NumberInput, nothing happens. This makes it impossible to start entering a value using the increment controls.

### Reproduction

```jsx
import { NumberInput } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  
  return (
    <NumberInput
      value={value}
      onChange={setValue}
      placeholder="Try clicking increment when empty"
    />
  );
}
```

Steps to reproduce:
1. Render a NumberInput with an empty value
2. Click the increment button or press arrow up
3. Nothing happens - the value stays empty

### Expected behavior

When the input is empty and I click the increment button, it should start incrementing from 0 (or the minimum value if set). This is the typical behavior for number inputs and was working in previous versions.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
