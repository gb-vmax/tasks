# Bug Report

### Describe the bug

The `JsonInput` component is incorrectly validating JSON strings. Empty/whitespace-only strings are being marked as invalid, and valid JSON is being marked as invalid while actual invalid JSON is being marked as valid.

### Reproduction

```jsx
import { JsonInput } from '@mantine/core';

function Demo() {
  return (
    <>
      {/* Empty string should be valid but shows error */}
      <JsonInput 
        value=""
        onChange={() => {}}
      />
      
      {/* Valid JSON shows as invalid */}
      <JsonInput 
        value='{"name": "test"}'
        onChange={() => {}}
      />
      
      {/* Invalid JSON shows as valid */}
      <JsonInput 
        value='{invalid json}'
        onChange={() => {}}
      />
    </>
  );
}
```

### Expected behavior

- Empty or whitespace-only strings should be considered valid
- Valid JSON strings should pass validation
- Invalid JSON strings should fail validation

The validation logic appears to be inverted - returning the opposite of what it should.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
