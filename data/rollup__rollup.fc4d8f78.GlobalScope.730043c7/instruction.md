# Bug Report

### Describe the bug

I'm encountering an issue where `undefined` is not being recognized as a global variable anymore. When I reference `undefined` in my code, it seems like the scope system isn't finding it properly, which is causing unexpected behavior in my bundled output.

### Reproduction

```js
// In my source code
function checkValue(val) {
  if (val === undefined) {
    return 'empty';
  }
  return 'has value';
}
```

When this gets processed, `undefined` doesn't seem to be treated as the built-in global variable. It's like the global scope isn't initialized with `undefined` anymore.

### Expected behavior

The `undefined` identifier should be recognized as a built-in global variable and handled appropriately by the scope system. Previously this worked fine, but something seems to have changed.

### Additional context

This might be related to how global variables are being registered in the scope. The issue appeared recently and is affecting code that relies on checking against `undefined`.

---
Repository: /testbed
