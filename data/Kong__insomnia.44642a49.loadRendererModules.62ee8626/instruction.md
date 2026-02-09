# Bug Report

### Describe the bug

After a recent update, plugins that use `app.__private.loadRendererModules()` are breaking. The function seems to have changed its behavior and is now returning modules with different property names than before.

### Reproduction

```js
// In a plugin's renderer code
const modules = await app.__private.loadRendererModules();

// This used to work but now returns undefined
console.log(modules.React); // undefined
console.log(modules.ReactDOM); // undefined
```

When I try to access `React` and `ReactDOM` from the returned object, they're coming back as undefined. This is breaking existing plugins that rely on these modules being available.

### Expected behavior

The `loadRendererModules()` function should return an object with `React` and `ReactDOM` properties like it did before, so existing plugins continue to work without modification.

### Additional context

This appears to have started happening after the latest update. My plugin was working fine previously and I haven't changed any code on my end. The function signature might have changed or there's an issue with how the modules are being cached/returned.

---
Repository: /testbed
