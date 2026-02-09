# Bug Report

### Describe the bug

I'm experiencing an issue with JSX member expressions where nested property access doesn't seem to be working correctly. When using JSX components with member expressions like `<Component.Nested />`, the bundler appears to be including/excluding code incorrectly, leading to runtime errors or unexpected behavior.

### Reproduction

```jsx
import * as Components from './components';

function App() {
  return (
    <div>
      <Components.Header />
      <Components.Content.Main />
    </div>
  );
}
```

When bundling the above code, the nested member expression `Components.Content.Main` doesn't resolve properly. The component either gets incorrectly tree-shaken out or the path isn't being tracked correctly through the member expression chain.

### Expected behavior

JSX member expressions should correctly resolve and include the referenced components in the bundle, regardless of nesting depth. Both `Components.Header` and `Components.Content.Main` should be properly included and accessible at runtime.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to recent changes in how member expressions are handled during tree-shaking.

---
Repository: /testbed
