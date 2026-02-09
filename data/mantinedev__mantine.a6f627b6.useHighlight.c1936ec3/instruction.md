# Bug Report

### Describe the bug

The `useHighlight` hook is returning a function reference instead of the actual highlighter function when used outside of a `CodeHighlightAdapterProvider`. This causes syntax highlighting to fail silently or throw errors when trying to use the returned value.

### Reproduction

```tsx
import { useHighlight } from '@mantine/code-highlight';

function MyComponent() {
  const highlight = useHighlight();
  
  // This fails because highlight is not the expected function
  const result = highlight('const x = 1;', 'javascript');
  
  return <div>{result}</div>;
}
```

When the component is used outside of a provider context, the hook should return a fallback highlighter function, but instead it's returning something that can't be called properly.

### Expected behavior

The hook should return a working highlighter function in all cases, falling back to the plain text adapter when used outside of a provider context.

### System Info
- @mantine/code-highlight version: latest
- React version: 18.x

---
Repository: /testbed
