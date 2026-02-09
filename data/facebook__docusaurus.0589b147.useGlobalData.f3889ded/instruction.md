# Bug Report

### Describe the bug

The `useGlobalData()` hook is returning undefined instead of the global data object. After a recent update, accessing global data in components causes runtime errors because the hook is trying to destructure a property that doesn't exist.

### Reproduction

```jsx
import useGlobalData from '@docusaurus/useGlobalData';

function MyComponent() {
  const globalData = useGlobalData();
  
  // globalData is undefined
  console.log(globalData); // undefined
  
  // This causes an error
  const pluginData = globalData['my-plugin'];
  
  return <div>...</div>;
}
```

### Expected behavior

`useGlobalData()` should return the global data object containing all plugin data, not undefined.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
