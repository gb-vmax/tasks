# Bug Report

### Describe the bug

I'm experiencing an issue with the `useUncontrolled` hook where state updates are not working as expected. When I try to update the value in an uncontrolled component, the value doesn't actually change - it just stays at its previous value.

### Reproduction

```jsx
import { useUncontrolled } from '@mantine/hooks';

function MyComponent() {
  const [value, handleChange] = useUncontrolled({
    defaultValue: 'initial',
    onChange: (val) => console.log('Changed to:', val)
  });

  return (
    <div>
      <p>Current value: {value}</p>
      <button onClick={() => handleChange('updated')}>
        Update Value
      </button>
    </div>
  );
}
```

### Expected behavior

When clicking the button, the value should update from 'initial' to 'updated', and the UI should reflect this change. The onChange callback should also be called with the new value.

### Actual behavior

The value remains stuck at 'initial' and never updates, even though the onChange callback is being triggered. It seems like the state is being set to the old value instead of the new one.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
