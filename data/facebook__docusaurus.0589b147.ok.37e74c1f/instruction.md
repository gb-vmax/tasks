# Bug Report

### Describe the bug

After a recent update, I'm getting an `Error: Not initialized` when using certain functions. The error seems to be coming from an internal validation check that wasn't there before.

### Reproduction

```js
// This now throws an error
ok()
```

The error message is:
```
Error: Not initialized
```

### Expected behavior

The function should execute without throwing an error. This used to work fine in previous versions and I haven't changed any initialization code on my end.

### Additional context

It looks like there's a new check for `this.initialized === false` that's causing this. I'm not sure what needs to be initialized or how to properly initialize it before calling this function.

---
Repository: /testbed
