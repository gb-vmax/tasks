# Bug Report

### Describe the bug

The `useGlobalData()` hook is returning the wrong data. Instead of returning the global data object, it seems to be returning the entire Docusaurus context object.

### Reproduction

```js
import useGlobalData from '@docusaurus/useGlobalData';

function MyComponent() {
  const globalData = useGlobalData();
  
  // Expected: globalData should be an object containing plugin data
  // Actual: globalData contains the entire context (siteConfig, etc.)
  console.log(globalData);
}
```

When I try to access plugin data using `useGlobalData()`, I get the full context object instead of just the `globalData` property. This breaks any code that expects to access plugin instances directly from the returned value.

### Expected behavior

`useGlobalData()` should return only the global data object containing plugin data, not the entire Docusaurus context.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
