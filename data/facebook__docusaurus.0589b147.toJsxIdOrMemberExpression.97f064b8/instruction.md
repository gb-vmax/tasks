# Bug Report

### Describe the bug

I'm encountering an issue with JSX member expressions where nested component references are not being generated correctly. When trying to use namespaced components (like `Foo.Bar` or `Foo.Bar.Baz`), the output seems to be reversed or incorrect.

### Reproduction

```jsx
// Trying to use a namespaced component
<Components.Icon />

// Or deeply nested
<UI.Components.Icon />
```

The generated code doesn't seem to properly construct the member expression chain. Instead of getting the correct nested structure, it appears to be building the expression in the wrong order or not at all.

### Expected behavior

When using namespaced JSX components like `Components.Icon`, the system should generate a proper JSX member expression that resolves to the correct component. For example:
- `Components.Icon` should resolve to accessing the `Icon` property of the `Components` object
- `UI.Components.Icon` should resolve to a nested member expression chain

### System Info
- @mdx-js/mdx version: 3.0.0

This seems to have broken recently. Previously, namespaced components were working fine but now they're not being resolved correctly.

---
Repository: /testbed
