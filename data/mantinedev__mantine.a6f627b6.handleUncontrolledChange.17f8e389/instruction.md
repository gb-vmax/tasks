# Bug Report

### Describe the bug

I'm experiencing an issue with the `useUncontrolled` hook where the internal state is being set incorrectly when used in uncontrolled mode. The hook seems to be updating the state with the wrong value from the callback arguments.

### Reproduction

```jsx
import { useUncontrolled } from '@mantine/hooks';

function MyComponent() {
  const [value, handleChange] = useUncontrolled({
    defaultValue: 'initial',
    onChange: (newValue) => console.log('Changed to:', newValue)
  });

  // When calling handleChange with a new value
  handleChange('updated value');
  
  // The internal state doesn't reflect the correct value
  console.log(value); // Expected: 'updated value', but shows something else
}
```

### Expected behavior

When using the hook in uncontrolled mode and calling the change handler with a new value, the internal state should be updated with that exact value. The first argument passed to the handler should become the new state value.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

This seems to have broken recently as it was working fine before. The uncontrolled state management appears to be using the wrong parameter from the callback arguments.

---
Repository: /testbed
