# Bug Report

### Describe the bug

I'm experiencing an issue with the `use-input-state` hook where checkbox inputs are not working correctly. When I try to use the hook with a checkbox, the state doesn't update properly when the checkbox is toggled.

### Reproduction

```jsx
import { useInputState } from '@mantine/hooks';

function MyComponent() {
  const [checked, setChecked] = useInputState(false);
  
  return (
    <input 
      type="checkbox" 
      checked={checked}
      onChange={setChecked}
    />
  );
}
```

When clicking the checkbox, the state remains unchanged and the checkbox doesn't toggle.

### Expected behavior

The checkbox should toggle on/off and the state should update accordingly with the checked value (true/false).

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
