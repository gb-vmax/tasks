# Bug Report

### Describe the bug

When using `useHighlight()` hook from the code-highlight package, syntax highlighting is not working at all. The hook seems to always return the plain text adapter instead of the actual highlighter from the context, even when a proper CodeHighlightProvider is configured.

### Reproduction

```tsx
import { CodeHighlightProvider, useHighlight } from '@mantine/code-highlight';

function MyComponent() {
  const highlight = useHighlight();
  
  // Expected: Should use the configured highlighter (e.g., Prism, Shiki)
  // Actual: Always returns plainTextAdapter, no syntax highlighting applied
  const result = highlight('const x = 5;', { language: 'javascript' });
  
  return <div>{result}</div>;
}

function App() {
  return (
    <CodeHighlightProvider adapter={myCustomAdapter}>
      <MyComponent />
    </CodeHighlightProvider>
  );
}
```

### Expected behavior

The `useHighlight()` hook should return the highlighter from the configured adapter in the context. Code should be properly syntax highlighted according to the adapter settings.

### Actual behavior

The hook always returns the plain text adapter, resulting in no syntax highlighting being applied regardless of the configured adapter.

---
Repository: /testbed
