# Bug Report

### Describe the bug

When using the `useHighlight` hook, I'm getting a "highlight is not a function" error. It seems like the hook is trying to call `highlight()` but it's not actually a function in the context object.

### Reproduction

```tsx
import { useHighlight } from '@mantine/code-highlight';

function MyComponent() {
  const highlight = useHighlight();
  
  // This throws: "highlight is not a function"
  const result = highlight('const x = 1;', 'javascript');
  
  return <div>{result}</div>;
}
```

### Expected behavior

The `useHighlight` hook should return a function that can be called to highlight code. The returned function should work without throwing errors.

### System Info
- @mantine/code-highlight version: latest
- React version: 18.x

---
Repository: /testbed
