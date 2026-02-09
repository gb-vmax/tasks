# Bug Report

### Describe the bug

The `useDocumentTitle` hook is not preserving whitespace in document titles. When setting a title with leading or trailing spaces, the spaces are being removed even though they should be kept as-is.

### Reproduction

```jsx
import { useDocumentTitle } from '@mantine/hooks';

function MyComponent() {
  // Title with intentional leading/trailing spaces
  useDocumentTitle('  My App  ');
  
  return <div>Check the document title</div>;
}
```

### Expected behavior

The document title should be set exactly as provided, including any leading or trailing whitespace. In the example above, `document.title` should be `'  My App  '` with the spaces preserved.

### Current behavior

The spaces are being stripped from the title, resulting in `'My App'` instead of `'  My App  '`.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
