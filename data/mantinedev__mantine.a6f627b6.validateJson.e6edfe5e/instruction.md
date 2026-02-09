# Bug Report

### Describe the bug

The `JsonInput` component is accepting invalid JSON strings without showing any validation errors. When I type malformed JSON, the input still appears valid and doesn't trigger any error state.

### Reproduction

```jsx
import { JsonInput } from '@mantine/core';

function Demo() {
  return (
    <JsonInput
      label="Your JSON"
      placeholder="Enter valid JSON"
      formatOnBlur
      autosize
      minRows={4}
    />
  );
}
```

Steps to reproduce:
1. Render a JsonInput component
2. Type invalid JSON like `{invalid json}` or `{"key": undefined}`
3. The component doesn't show any validation error

### Expected behavior

The component should validate the JSON input and display an error state when the JSON is malformed or invalid. Invalid JSON should be rejected and the component should indicate to the user that the input is not valid.

### Additional context

Also noticed that whitespace-only strings (like `"   "`) are being treated as valid JSON when they should probably be considered empty/invalid.

---
Repository: /testbed
