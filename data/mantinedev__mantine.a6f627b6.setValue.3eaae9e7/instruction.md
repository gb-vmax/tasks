# Bug Report

### Describe the bug
I'm encountering an issue with the `use-input-state` hook where checkbox inputs are not updating correctly. When I toggle a checkbox, the state gets set to the input's value string instead of the boolean checked state.

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
- Expected: `checked` state should be `true` or `false` (boolean)
- Actual: `checked` state becomes `"on"` (the default value attribute)

### Expected behavior
Checkbox inputs should correctly update the state with their `checked` property (boolean value), not their `value` property (string).

Regular text inputs still work fine - this only affects checkboxes.

---
Repository: /testbed
