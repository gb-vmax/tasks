# Bug Report

### Describe the bug

The `useUncontrolled` hook is not updating the internal state correctly when used in uncontrolled mode. When the onChange callback is provided, the state value passed to it is stale (the old value instead of the new value), and the internal state only updates if onChange is defined.

### Reproduction

```tsx
import { useUncontrolled } from '@mantine/hooks';

function MyComponent() {
  const [value, handleChange] = useUncontrolled({
    defaultValue: 'initial',
    onChange: (val) => console.log('Changed to:', val)
  });

  // When calling handleChange('new value')
  // Console logs: "Changed to: initial" (should be "new value")
  // And if onChange is undefined, the state doesn't update at all

  return (
    <input 
      value={value} 
      onChange={(e) => handleChange(e.target.value)} 
    />
  );
}
```

### Expected behavior

1. The onChange callback should receive the **new** value, not the current/old value
2. The internal state should update regardless of whether onChange is provided or not

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
