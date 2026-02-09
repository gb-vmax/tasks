# Bug Report

### Describe the bug

I'm encountering an issue with JSX member expressions where properties are not being properly tracked during tree-shaking. When using nested member expressions in JSX (e.g., `<Component.SubComponent />`), the bundler seems to be including more code than necessary or potentially breaking the inclusion logic.

### Reproduction

```jsx
import * as Components from './components';

// Using a member expression in JSX
function App() {
  return <Components.Button />;
}
```

When bundling code that uses JSX member expressions like `Component.Property`, the property path tracking appears to be incorrect. The issue manifests when trying to access nested component properties through member expressions.

### Expected behavior

The bundler should correctly track which properties are being accessed on JSX member expressions and include only the necessary code paths. Property names should be properly propagated through the inclusion path.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
