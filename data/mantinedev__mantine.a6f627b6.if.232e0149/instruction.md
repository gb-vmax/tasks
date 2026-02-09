# Bug Report

### Describe the bug

When passing string values directly to Combobox data, the selected value is not being set correctly. The label displays fine, but the actual value becomes empty instead of using the string itself.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

const data = ['React', 'Vue', 'Angular'];

function Demo() {
  const [value, setValue] = useState('React');
  
  return (
    <Combobox data={data} value={value} onChange={setValue} />
  );
}

// When selecting an option, the value becomes '' instead of 'React'
// The dropdown shows the correct labels but the value prop receives empty string
```

### Expected behavior

When using string array format for Combobox data, each string should be used as both the value and label. Selecting "React" should set the value to "React", not an empty string.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
