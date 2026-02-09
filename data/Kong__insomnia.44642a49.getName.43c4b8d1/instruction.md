# Bug Report

### Describe the bug
When using the plugin API's `request.getName()` method, the returned request name has an unexpected trailing space appended to it. This breaks string comparisons and any logic that depends on exact name matching.

### Reproduction
```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const name = context.request.getName();
    console.log(`"${name}"`); // Shows: "My Request "
    console.log(name === "My Request"); // Returns false, expected true
  }
];
```

### Expected behavior
The `getName()` method should return the request name without any trailing whitespace. If the original name is "My Request", the method should return exactly "My Request", not "My Request ".

### System Info
- Insomnia version: latest
- Plugin API: request context

---
Repository: /testbed
