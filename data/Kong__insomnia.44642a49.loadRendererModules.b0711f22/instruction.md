# Bug Report

### Describe the bug

After a recent update, plugins that use `app.__private.loadRendererModules()` are failing because the function is returning an object with an unexpected structure. The returned object now includes a `_metadata` property that wasn't there before, which is breaking existing plugins that expect only `ReactDOM` and `React` properties.

### Reproduction

```js
// In a plugin context
const modules = await app.__private.loadRendererModules();

// This used to work but now fails
const { ReactDOM, React } = modules;

// ReactDOM and React are now undefined because the structure changed
console.log(ReactDOM); // undefined
console.log(React); // undefined

// The actual structure now looks like:
// {
//   ReactDOM: ...,
//   React: ...,
//   _metadata: { ... }
// }
```

### Expected behavior

The function should return an object with only `ReactDOM` and `React` properties to maintain backward compatibility with existing plugins. Any additional metadata should not be included in the return value or should be added in a way that doesn't break destructuring.

### System Info
- Insomnia version: latest
- Platform: Windows/Mac/Linux

This is breaking several of our custom plugins that rely on loading React modules for rendering custom UI components.

---
Repository: /testbed
