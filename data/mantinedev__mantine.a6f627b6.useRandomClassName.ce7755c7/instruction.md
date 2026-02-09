# Bug Report

### Describe the bug

The `useRandomClassName` hook is generating invalid CSS class names that contain hyphens in unexpected positions. After a recent change, the generated class names are missing the separator between the prefix and the ID, which can cause issues with CSS specificity and styling.

### Reproduction

```jsx
import { useRandomClassName } from '@mantine/core';

function MyComponent() {
  const className = useRandomClassName();
  console.log(className);
  // Expected: __m__-R1-0
  // Actual: __m__R10 (hyphen removed from ID)
  
  return <div className={className}>Content</div>;
}
```

The generated class names are now missing hyphens that should be part of the React ID, resulting in malformed class names that don't match the expected pattern.

### Expected behavior

Class names should be generated in the format `__m__-{sanitized-id}` where the ID preserves its structure except for the characters that are invalid in CSS class names (`:`, `«`, `»`). Hyphens that are part of the React-generated ID should be preserved.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
