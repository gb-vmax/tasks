# Bug Report

### Describe the bug

When using `Checkbox` component within a `Checkbox.Group`, the group's `onChange` handler is not being called if an individual checkbox doesn't have its own `onChange` prop defined.

### Reproduction

```jsx
import { Checkbox } from '@mantine/core';

function App() {
  const [value, setValue] = useState([]);

  return (
    <Checkbox.Group 
      value={value} 
      onChange={setValue}
    >
      <Checkbox value="react" label="React" />
      <Checkbox value="vue" label="Vue" />
    </Checkbox.Group>
  );
}
```

In this example, clicking on any checkbox doesn't update the group's value state. The group's `onChange` handler is never triggered.

### Expected behavior

The `Checkbox.Group` `onChange` should be called when any checkbox in the group is toggled, regardless of whether individual checkboxes have their own `onChange` handlers or not.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
