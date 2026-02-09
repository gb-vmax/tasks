# Bug Report

### Describe the bug

The `useGlobalData()` hook is returning incorrect data after a recent change. Instead of returning the global data object, it appears to be returning either `undefined` or the entire Docusaurus context object.

### Reproduction

```js
import useGlobalData from '@docusaurus/useGlobalData';

function MyComponent() {
  const globalData = useGlobalData();
  console.log(globalData); // Expected: global data object, Actual: undefined or context object
  
  // Trying to access plugin data fails
  const myPluginData = globalData?.['my-plugin']?.default;
  // myPluginData is undefined
}
```

### Expected behavior

`useGlobalData()` should return the `globalData` object from the Docusaurus context, which contains data from all plugins. The hook should provide access to plugin instance data through the returned object.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking my site as I rely on accessing plugin data through this hook. Any component using `useGlobalData()` is now unable to access the expected data structure.

---
Repository: /testbed
