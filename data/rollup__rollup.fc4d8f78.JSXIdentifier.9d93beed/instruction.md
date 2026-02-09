# Bug Report

### Describe the bug

JSX components with lowercase names are being incorrectly treated as native HTML elements instead of custom components. This causes the bundler to not properly resolve component references.

### Reproduction

```jsx
// Component defined with lowercase name
const myComponent = () => <div>Hello</div>;

// Usage in JSX
function App() {
  return <myComponent />;
}
```

When bundling this code, `myComponent` is treated as a native element (like `div` or `span`) rather than as a reference to the custom component. This means the component reference isn't included in the bundle correctly.

### Expected behavior

Custom components should be recognized as references regardless of whether their name starts with an uppercase or lowercase letter. The component should be properly included in the output bundle and function correctly.

### Additional context

This seems to affect how JSX identifiers are categorized. Components with names that don't follow the typical PascalCase convention (starting with uppercase) are misidentified, leading to incorrect bundling behavior.

---
Repository: /testbed
