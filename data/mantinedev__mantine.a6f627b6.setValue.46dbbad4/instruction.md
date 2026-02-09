# Bug Report

### Describe the bug

The `use-input-state` hook is not handling text inputs correctly. When I use this hook with a regular text input field, the value doesn't update properly. It seems like the hook is trying to read the `checked` property instead of the `value` property from text inputs.

### Reproduction

```jsx
import { useInputState } from '@mantine/hooks';

function MyComponent() {
  const [value, onChange] = useInputState('');

  return (
    <input 
      type="text" 
      value={value} 
      onChange={onChange} 
    />
  );
}
```

When typing into the text input, the value doesn't update as expected. The input field remains empty or shows unexpected behavior.

### Expected behavior

The text input should update normally, capturing the typed value from `event.currentTarget.value`. This was working fine in previous versions.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
