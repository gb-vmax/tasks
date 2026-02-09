# Bug Report

### Describe the bug

The `set` method on the Variables object is not working as expected after a recent update. When trying to set a variable without specifying a scope, it seems like the variable is being set in the wrong place or the behavior has changed.

### Reproduction

```js
const variables = new Variables(/* ... */);

// This used to work but now behaves differently
variables.set('myVar', 'someValue');

// The variable doesn't seem to be accessible where expected
console.log(variables.get('myVar')); // undefined or unexpected value
```

### Expected behavior

Setting a variable without specifying a scope should work the same way as before. The variable should be accessible via `get()` after being set.

### Additional context

This seems to have broken after some recent changes to the variables handling. The `set` method signature might have changed but I'm not sure what the correct usage is now.

---
Repository: /testbed
