# Bug Report

### Describe the bug

The `useGlobalData()` hook is returning incorrect data structure after a recent update. It seems like the hook is now returning a nested object structure instead of the global data directly, causing issues when trying to access plugin data.

### Reproduction

```js
import useGlobalData from '@docusaurus/useGlobalData';

function MyComponent() {
  const globalData = useGlobalData();
  
  // This used to work but now returns undefined
  const pluginData = globalData['my-plugin'];
  console.log(pluginData); // undefined
  
  // The actual data seems to be nested somewhere else
  console.log(globalData); // Shows unexpected structure
}
```

### Expected behavior

`useGlobalData()` should return the global data object directly, allowing access to plugin data via `globalData[pluginName]` as documented.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
