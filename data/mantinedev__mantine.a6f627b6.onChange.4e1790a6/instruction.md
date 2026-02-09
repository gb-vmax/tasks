# Bug Report

### Describe the bug

When using the `Switch` component within a `Switch.Group` context, the `onChange` callback is not being called properly. The context's `onChange` handler only fires when the individual Switch has its own `onChange` prop defined, which breaks the expected behavior of the group.

### Reproduction

```jsx
import { Switch } from '@mantine/core';

function App() {
  const [value, setValue] = useState([]);
  
  return (
    <Switch.Group value={value} onChange={setValue}>
      <Switch value="option1" label="Option 1" />
      <Switch value="option2" label="Option 2" />
    </Switch.Group>
  );
}
```

Steps to reproduce:
1. Create a Switch.Group with an onChange handler
2. Add Switch components without individual onChange handlers
3. Try to toggle the switches
4. The group's onChange is never called and the state doesn't update

### Expected behavior

The Switch.Group's `onChange` should be triggered whenever any Switch in the group is toggled, regardless of whether individual switches have their own `onChange` handlers. The group should manage the state of all switches within it.

### Additional context

This seems to have broken recently. The switches work fine when used standalone with their own onChange handlers, but the group functionality is completely broken now.

---
Repository: /testbed
