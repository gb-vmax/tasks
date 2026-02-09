# Bug Report

### Describe the bug

When using Radio components with `onChange` handlers, the context-level `onChange` (from `Radio.Group`) is not being called when the individual Radio's `onChange` handler doesn't call `event.preventDefault()`. This breaks the expected behavior where both the individual Radio's `onChange` and the group's `onChange` should be triggered.

### Reproduction

```jsx
import { Radio } from '@mantine/core';

function App() {
  const [value, setValue] = React.useState('');

  return (
    <Radio.Group value={value} onChange={setValue}>
      <Radio 
        value="option1" 
        onChange={(e) => {
          console.log('Individual onChange called');
          // Not calling e.preventDefault()
        }} 
      />
      <Radio value="option2" />
    </Radio.Group>
  );
}
```

### Expected behavior

When clicking on the first radio button:
1. The individual `onChange` handler should be called
2. The `Radio.Group`'s `onChange` handler should also be called
3. The selected value should update in the group

### Actual behavior

When clicking on the first radio button:
1. The individual `onChange` handler is called
2. The `Radio.Group`'s `onChange` handler is **NOT** called (unless `event.preventDefault()` is explicitly called)
3. The selected value doesn't update in the group

This seems backwards - the group's onChange should fire by default, not only when preventDefault is called.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
