# Bug Report

### Describe the bug

The `newDefaultRegistry()` function is returning a string instead of an object. When trying to use the hotkey registry, I'm getting errors because the code expects an object but receives a JSON string.

### Reproduction

```js
const registry = newDefaultRegistry();

// This fails because registry is a string, not an object
console.log(registry.workspace_showSettings); // TypeError: Cannot read property 'workspace_showSettings' of undefined

// registry is actually a JSON string
console.log(typeof registry); // "string"
console.log(registry); // "[object Object]" or similar stringified output
```

### Expected behavior

`newDefaultRegistry()` should return a cloned `HotKeyRegistry` object that can be used to access hotkey configurations. The function should return the parsed JSON object, not a stringified version of it.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
