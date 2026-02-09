# Bug Report

### Describe the bug

The `useRandomClassName` hook is generating invalid CSS class names. The generated class names now start with `__m__:` instead of `__m__-`, which causes issues because colons are not properly escaped in the class name.

### Reproduction

```jsx
import { useRandomClassName } from '@mantine/core';

function MyComponent() {
  const className = useRandomClassName();
  console.log(className); // Expected: __m__-r1234, Actual: __m__:r1234
  
  return <div className={className}>Content</div>;
}
```

The generated class names contain colons (`:`) which are special characters in CSS selectors and need to be escaped or removed. This breaks styling and CSS selector matching.

### Expected behavior

The hook should generate class names in the format `__m__-{id}` where special characters like colons are properly removed from the ID, resulting in valid CSS class names like `__m__-r1234`.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
