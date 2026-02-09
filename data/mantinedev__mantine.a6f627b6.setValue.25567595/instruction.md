# Bug Report

### Describe the bug

I'm experiencing an issue with `useInputState` where unchecking a checkbox doesn't update the state value. When I check a checkbox, the state updates correctly to `true`, but when I uncheck it, the state remains `true` instead of updating to `false`.

### Reproduction

```jsx
import { useInputState } from '@mantine/hooks';

function MyComponent() {
  const [checked, setChecked] = useInputState(false);
  
  return (
    <div>
      <input 
        type="checkbox" 
        checked={checked} 
        onChange={setChecked} 
      />
      <p>Current value: {String(checked)}</p>
    </div>
  );
}
```

Steps to reproduce:
1. Render a checkbox with `useInputState`
2. Check the checkbox - state updates to `true` ✓
3. Uncheck the checkbox - state stays `true` ✗

The checkbox appears unchecked visually but the state value doesn't change back to `false`.

### Expected behavior

When unchecking a checkbox, the state should update to `false`. Both checking and unchecking should properly update the state value.

Also noticed a similar issue with text inputs - when clearing an input field (making it empty), the state doesn't update to an empty string. It keeps the previous non-empty value.

---
Repository: /testbed
