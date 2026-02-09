# Bug Report

### Describe the bug

When using the `Switch` component within a context (like `Switch.Group`), the `onChange` handler doesn't receive the change event properly. The context's `onChange` is being called without passing the event parameter, which breaks the expected behavior when trying to access event properties.

### Reproduction

```jsx
import { Switch } from '@mantine/core';

function MyComponent() {
  const handleChange = (event) => {
    console.log(event.currentTarget.checked); // event is undefined
    console.log(event.currentTarget.value); // throws error
  };

  return (
    <Switch.Group onChange={handleChange}>
      <Switch value="option1" label="Option 1" />
      <Switch value="option2" label="Option 2" />
    </Switch.Group>
  );
}
```

### Expected behavior

The `onChange` handler should receive the change event object so that I can access properties like `event.currentTarget.checked` and `event.currentTarget.value`. This worked correctly in previous versions.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
