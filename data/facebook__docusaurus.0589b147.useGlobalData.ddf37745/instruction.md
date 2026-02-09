# Bug Report

### Describe the bug

The `useGlobalData()` hook is returning the wrong data structure. Instead of returning the global data object, it appears to be returning the entire Docusaurus context object.

### Reproduction

```js
import useGlobalData from '@docusaurus/useGlobalData';

function MyComponent() {
  const globalData = useGlobalData();
  
  // Expected: globalData should contain plugin data
  // Actual: globalData contains the entire context object
  console.log(globalData);
  
  // This breaks when trying to access plugin data
  const myPluginData = globalData['my-plugin'];
  // TypeError: Cannot read property 'my-plugin' of undefined
}
```

### Expected behavior

`useGlobalData()` should return the `globalData` object that contains all plugin instance data, not the entire Docusaurus context.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
