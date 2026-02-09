# Bug Report

### Describe the bug

I'm encountering an issue with JSX native elements where they seem to be getting incorrectly treated as variable references. When using native HTML elements in JSX (like `<div>`, `<span>`, etc.), the compiler appears to be looking them up as if they were component references, which causes unexpected behavior.

### Reproduction

```jsx
function MyComponent() {
  return (
    <div>
      <span>Hello World</span>
    </div>
  );
}
```

When compiling the above code, native HTML elements like `div` and `span` are being processed as if they need to be resolved from the scope, rather than being recognized as native DOM elements.

### Expected behavior

Native HTML elements should be identified as `NativeElementName` type and not attempt to resolve them as variables from the scope. They should be treated differently from custom component references.

### Additional context

This appears to affect all native HTML elements used in JSX syntax. The issue is that the compiler is trying to find these native element names in the variable scope when it shouldn't be doing so.

---
Repository: /testbed
