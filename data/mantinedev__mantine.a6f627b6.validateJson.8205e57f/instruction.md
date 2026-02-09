# Bug Report

### Describe the bug

I'm experiencing an issue with the `JsonInput` component where whitespace-only strings (like spaces, tabs, or newlines) are being treated as valid JSON input. According to JSON specification, whitespace-only strings should not be considered valid JSON.

### Reproduction

```jsx
import { JsonInput } from '@mantine/core';

function Demo() {
  return (
    <JsonInput
      label="JSON Input"
      placeholder="Enter JSON"
      validationError="Invalid JSON"
      formatOnBlur
    />
  );
}
```

Steps to reproduce:
1. Create a JsonInput component
2. Enter only whitespace characters (spaces, tabs, or newlines) into the input field
3. The input is treated as valid even though it contains no actual JSON data

### Expected behavior

Whitespace-only strings should be treated as invalid JSON input and trigger a validation error. Only truly empty strings (zero length) or valid JSON should be accepted.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
