# Bug Report

### Describe the bug

The JsonInput component is accepting invalid JSON strings as valid input. When I type malformed JSON or leave the input empty, it's not showing any validation errors like it should.

### Reproduction

```jsx
import { JsonInput } from '@mantine/core';

function Demo() {
  return (
    <JsonInput
      label="Your JSON"
      placeholder="Enter JSON"
      validationError="Invalid JSON"
      formatOnBlur
      autosize
      minRows={4}
    />
  );
}
```

Steps to reproduce:
1. Create a JsonInput component with validation
2. Type invalid JSON like `{invalid json}` or `not json at all`
3. The component doesn't show any validation error
4. Also happens when the input is completely empty - no error is displayed

### Expected behavior

- Invalid JSON syntax should trigger a validation error
- Empty input should be treated as valid (or configurable)
- Only properly formatted JSON should be accepted without errors

Currently it seems like the validation is inverted - it's accepting everything as valid when it should be rejecting malformed JSON.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox/Chrome

---
Repository: /testbed
