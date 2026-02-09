# Bug Report

### Describe the bug

When using `Switch` component with an `onChange` handler outside of a `Switch.Group` context, the `onChange` callback is no longer being triggered. The switch state updates visually, but custom `onChange` handlers are silently ignored when the switch is used standalone (not in a group).

### Reproduction

```jsx
import { Switch } from '@mantine/core';

function MyComponent() {
  const [checked, setChecked] = useState(false);
  
  const handleChange = (event) => {
    console.log('onChange called:', event.target.checked);
    setChecked(event.target.checked);
  };
  
  return (
    <Switch 
      checked={checked}
      onChange={handleChange}
      label="My Switch"
    />
  );
}
```

### Expected behavior

The `onChange` handler should be called whenever the switch is toggled, regardless of whether it's used standalone or within a `Switch.Group`. The console should log the change and the state should update.

### Actual behavior

When clicking the switch, the `onChange` handler is never called. The switch appears to toggle visually but the custom handler doesn't fire and state doesn't update.

This works fine when the Switch is used inside a `Switch.Group`, but breaks for standalone usage.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
