# Bug Report

### Describe the bug

I'm experiencing an issue with the `use-input-state` hook when handling checkbox inputs. When I toggle a checkbox, the state is being set to the string value instead of the boolean checked state.

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

When clicking the checkbox:
- Expected: `checked` should be `true` or `false`
- Actual: `checked` is set to a string value instead of the boolean checked state

### Expected behavior

The hook should correctly handle checkbox inputs by reading the `checked` property rather than the `value` property, so the state reflects the actual checked state (true/false) of the checkbox.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
