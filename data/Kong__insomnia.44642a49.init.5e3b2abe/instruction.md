# Bug Report

### Describe the bug

I'm experiencing an issue when creating new environments. The environment's `data` field is being initialized as `null` instead of an empty object, which causes problems when trying to add environment variables.

### Reproduction

```js
// Create a new environment
const env = init();

// Try to add a variable
env.data.myVar = 'value'; // TypeError: Cannot set property 'myVar' of null
```

When I create a new environment and try to set variables on it, I get a null reference error because `data` is `null` instead of an empty object `{}`.

### Expected behavior

The `data` field should be initialized as an empty object `{}` so that environment variables can be added immediately after creation without having to manually initialize the object first.

### Additional context

This seems to have started happening recently. Previously, new environments would have an empty object for `data` by default, which allowed variables to be added right away.

---
Repository: /testbed
