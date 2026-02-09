# Bug Report

### Describe the bug

I'm experiencing an issue with JSX fragment rendering where nested fragment references are not being generated correctly. When using JSX fragments with a custom JSX import source, the fragment variable name appears to be duplicated or incorrectly sliced in the output code.

### Reproduction

```jsx
// Using a custom JSX import source
/** @jsxImportSource custom-jsx */

function MyComponent() {
  return (
    <>
      <div>Content</div>
    </>
  );
}
```

When the fragment is processed, the generated code seems to have issues with how the fragment variable is being constructed, particularly when dealing with nested properties in the fragment reference.

### Expected behavior

The JSX fragment should be transformed correctly using the proper fragment reference from the custom JSX import source. The fragment variable should be generated with the correct property access chain without any duplication or missing parts.

### Additional context

This seems to affect cases where the fragment reference includes nested properties (e.g., `React.Fragment` or similar patterns with custom JSX libraries). The transformation should preserve the complete property chain correctly.

---
Repository: /testbed
