# Bug Report

### Describe the bug

I'm encountering an issue with JSX member expressions when using namespaced or nested component names. The component hierarchy appears to be reversed, causing incorrect rendering or component resolution.

### Reproduction

When trying to use a component like `Ui.Card.Header`, the member expression is being constructed incorrectly. Instead of resolving to the proper nested structure, the components are being accessed in reverse order.

```jsx
// Using a namespaced component
<Ui.Card.Header />

// Expected: Ui -> Card -> Header
// Actual: The nesting appears reversed
```

This affects any JSX element that uses dot notation for component names. The issue seems to impact how the AST is constructed for these member expressions.

### Expected behavior

JSX member expressions should be built in the correct order, with the outermost object first, followed by nested properties in left-to-right order. For example, `Ui.Card.Header` should resolve as `Ui` (object) -> `Card` (property) -> `Header` (property).

### Additional context

This appears to be a regression as it was working correctly in previous versions. The problem manifests when rendering components that rely on namespaced naming conventions.

---
Repository: /testbed
