# Bug Report

### Describe the bug

JSX components are not being included in the bundle when they should be. It appears that JSX identifiers are being incorrectly excluded during tree-shaking, causing components to be missing from the output even when they're clearly used in the code.

### Reproduction

```jsx
import React from 'react';
import MyComponent from './MyComponent';

function App() {
  return (
    <div>
      <MyComponent />
    </div>
  );
}
```

When bundling this code, `MyComponent` gets tree-shaken out of the final bundle even though it's clearly being used. The resulting bundle throws a runtime error because the component is undefined.

### Expected behavior

JSX components that are referenced in the code should be included in the bundle. The component should render correctly without being removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
