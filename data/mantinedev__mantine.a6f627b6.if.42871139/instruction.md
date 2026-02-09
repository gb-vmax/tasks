# Bug Report

### Describe the bug

The `focus` method in TimePicker is not working correctly for the hours field. When trying to programmatically focus the hours input, nothing happens and the focus remains on the current element.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';
import { useRef } from 'react';

function MyComponent() {
  const timePickerRef = useRef(null);
  
  return (
    <div>
      <TimePicker ref={timePickerRef} />
      <button onClick={() => {
        // This should focus the hours input but doesn't work
        timePickerRef.current?.focus('hours');
      }}>
        Focus Hours
      </button>
    </div>
  );
}
```

### Expected behavior

When calling the `focus` method with `'hours'` as the parameter, the hours input field should receive focus. Instead, the focus behavior seems inverted - the hours field gets focused when any other field name is passed, but not when 'hours' is explicitly specified.

### System Info
- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
