# Bug Report

### JSX identifier variables not being included in module output

I've encountered an issue where JSX identifiers are not being properly included in the bundled output. When using JSX components, the variable references seem to be getting skipped during the inclusion phase.

### Reproduction

```jsx
import { MyComponent } from './components';

function App() {
  return <MyComponent />;
}
```

After bundling, the `MyComponent` reference is missing from the output, causing runtime errors about undefined variables.

### Expected behavior

The JSX identifier should be properly tracked and included in the module, ensuring that all component references are present in the final bundle.

### Additional context

This seems to affect JSX identifiers specifically. Regular JavaScript identifiers appear to work fine. The issue might be related to how the inclusion logic handles the `included` flag for JSX nodes.

---
Repository: /testbed
