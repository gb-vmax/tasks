# Bug Report

### Describe the bug

I'm experiencing an issue with JSX identifier handling where native HTML elements (like `div`, `span`, etc.) are being treated as references to variables instead of being recognized as native elements. This causes the bundler to try to resolve them as imports, which leads to incorrect behavior.

### Reproduction

```jsx
function Component() {
  return <div>Hello World</div>
}
```

When bundling this code, the `div` identifier is being treated as if it's a variable reference that needs to be resolved from the scope, rather than being recognized as a native HTML element name.

### Expected behavior

Native HTML element names in JSX should be recognized as native elements and not treated as variable references. The bundler should not attempt to find them in the scope or add them as references.

### Additional context

This appears to affect all native HTML elements used in JSX. Custom components (capitalized names) work correctly, but lowercase native elements are incorrectly processed.

---
Repository: /testbed
