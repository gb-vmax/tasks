# Bug Report

### Describe the bug

The `useRandomClassName` hook is generating invalid CSS class names that contain characters which are not properly escaped. This causes issues when these class names are used in selectors or when the styles are applied to elements.

### Reproduction

```jsx
import { useRandomClassName } from '@mantine/core';

function MyComponent() {
  const className = useRandomClassName();
  console.log(className); // Outputs something like: __m__:r1:
  
  return <div className={className}>Content</div>;
}
```

The generated class names include colon characters (`:`) which are special characters in CSS and need to be escaped when used in selectors. This breaks styling and querySelector operations.

### Expected behavior

The hook should generate valid CSS class names without special characters that require escaping. Class names should only contain alphanumeric characters, hyphens, and underscores.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
