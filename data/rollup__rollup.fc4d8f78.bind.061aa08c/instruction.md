# Bug Report

### Describe the bug
When using JSX with native HTML elements, they are incorrectly being treated as custom components. This causes native elements to be bundled/referenced incorrectly in the output.

### Reproduction
```jsx
// Example JSX code
function MyComponent() {
  return (
    <div>
      <span>Hello</span>
      <button>Click me</button>
    </div>
  );
}
```

When bundling this code, native HTML elements like `div`, `span`, and `button` are being treated as if they're custom component references instead of native elements. This results in incorrect output where these elements may be included in the bundle as if they need to be resolved as variables.

### Expected behavior
Native HTML elements (div, span, button, etc.) should be recognized as native elements and not treated as component references that need variable resolution. The bundler should distinguish between custom components and standard HTML elements.

### Additional context
This appears to affect all standard HTML element names in JSX. Custom components (capitalized names) seem to work fine, but lowercase native element names are being misidentified.

---
Repository: /testbed
