# Bug Report

### Describe the bug

When using `Checkbox` components within a `Checkbox.Group`, the individual checkbox `onChange` handlers are not being called properly. The event object is not being passed to the individual checkbox's `onChange` callback, which breaks any custom logic that depends on the event.

### Reproduction

```jsx
import { Checkbox } from '@mantine/core';

function MyComponent() {
  const [values, setValues] = useState([]);

  return (
    <Checkbox.Group value={values} onChange={setValues}>
      <Checkbox 
        value="option1" 
        label="Option 1"
        onChange={(event) => {
          // This callback doesn't receive the event properly
          console.log('Checked:', event.currentTarget.checked);
          console.log('Value:', event.currentTarget.value);
        }}
      />
      <Checkbox 
        value="option2" 
        label="Option 2"
        onChange={(event) => {
          // Custom validation or side effects don't work
          if (event.currentTarget.checked) {
            // Do something
          }
        }}
      />
    </Checkbox.Group>
  );
}
```

### Expected behavior

The individual checkbox `onChange` handler should receive the change event object as a parameter, allowing access to `event.currentTarget.checked`, `event.currentTarget.value`, etc. Both the group's `onChange` and the individual checkbox's `onChange` should be called with the proper event object.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
