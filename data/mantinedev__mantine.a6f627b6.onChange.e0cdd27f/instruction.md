# Bug Report

### Describe the bug

When using Radio components inside a RadioGroup, the radio selection behavior is broken. Clicking on a radio button prevents the selection from changing, making it impossible to switch between different radio options.

### Reproduction

```jsx
import { Radio, RadioGroup } from '@mantine/core';

function App() {
  const [value, setValue] = useState('react');

  return (
    <RadioGroup value={value} onChange={setValue}>
      <Radio value="react" label="React" />
      <Radio value="vue" label="Vue" />
      <Radio value="angular" label="Angular" />
    </RadioGroup>
  );
}
```

Steps to reproduce:
1. Create a RadioGroup with multiple Radio components
2. Try to click on any radio button
3. The selection doesn't change - the radio button stays in its current state

### Expected behavior

Clicking on a radio button should select it and update the RadioGroup's value. The onChange handler should be called and the UI should reflect the new selection.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

This appears to have started recently, possibly after a recent update. The radio buttons are completely non-functional when used within a RadioGroup context.

---
Repository: /testbed
