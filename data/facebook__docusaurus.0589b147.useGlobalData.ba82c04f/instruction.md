# Bug Report

### Describe the bug

After a recent update, `useGlobalData()` is returning `undefined` instead of the expected global data object. This is breaking components that rely on accessing plugin data through this hook.

### Reproduction

```js
import useGlobalData from '@docusaurus/useGlobalData';

function MyComponent() {
  const globalData = useGlobalData();
  console.log(globalData); // prints undefined instead of global data object
  
  // This causes errors when trying to access plugin data
  const myPluginData = globalData?.myPlugin; // globalData is undefined
}
```

### Expected behavior

`useGlobalData()` should return the global data object containing all plugin data, not `undefined`. Previously this was working correctly and components could access plugin instance data through the returned object.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
