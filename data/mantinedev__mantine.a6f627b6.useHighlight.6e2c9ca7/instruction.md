# Bug Report

### Describe the bug

When using the `useHighlight` hook from `@mantine/code-highlight`, I'm getting a TypeError when trying to use the returned highlight function. It seems like the hook is returning a function instead of the expected highlighter object, causing issues when attempting to call methods on it.

### Reproduction

```tsx
import { useHighlight } from '@mantine/code-highlight';

function MyComponent() {
  const highlight = useHighlight();
  
  // This throws an error - highlight is not callable
  const result = highlight('const x = 1;', 'javascript');
  
  return <div>{result}</div>;
}
```

### Expected behavior

The `useHighlight` hook should return a highlighter object that can be used directly to highlight code, not a function that needs to be called first.

### System Info
- @mantine/code-highlight version: latest
- React version: 18.x

---
Repository: /testbed
