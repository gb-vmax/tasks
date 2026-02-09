# Bug Report

### Describe the bug

The TimePicker component's focus management is broken. When trying to focus on the hours field programmatically, it doesn't receive focus. Instead, the focus behavior seems inverted - focusing on any field other than hours causes the hours field to be focused instead.

### Reproduction

```tsx
import { TimePicker } from '@mantine/dates';
import { useRef } from 'react';

function MyComponent() {
  const ref = useRef<HTMLInputElement>(null);
  
  return (
    <div>
      <TimePicker ref={ref} />
      <button onClick={() => {
        // Try to focus the hours field
        // Expected: hours field gets focus
        // Actual: nothing happens
      }}>
        Focus Hours
      </button>
    </div>
  );
}
```

When attempting to focus the hours input field, nothing happens. However, if you try to focus on minutes or seconds fields, the hours field gets focused instead, which is completely backwards.

### Expected behavior

Calling focus on the hours field should actually focus the hours input, not ignore it. The focus should go to the field that was requested, not a different one.

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
