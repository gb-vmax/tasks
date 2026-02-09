# Bug Report

### Describe the bug

I'm experiencing an issue with `using` and `async using` declarations where the wrong disposal method is being called. When I use `using` declarations, it seems like the async disposal path is being triggered instead of the sync one, and vice versa for `async using`.

### Reproduction

```js
// using declaration calls async dispose instead of sync dispose
using resource = getResource();
// Expected: Symbol.dispose to be called
// Actual: Symbol.asyncDispose is being called

// async using declaration calls sync dispose instead of async dispose  
async using asyncResource = getAsyncResource();
// Expected: Symbol.asyncDispose to be called
// Actual: Symbol.dispose is being called
```

### Expected behavior

- `using` declarations should call `Symbol.dispose` on the resource
- `async using` declarations should call `Symbol.asyncDispose` on the resource

The disposal methods appear to be swapped - `using` is calling the async disposal path and `async using` is calling the sync disposal path.

### Additional context

This seems to have broken recently. The disposal mechanism worked correctly before but now the wrong symbols are being used for cleanup.

---
Repository: /testbed
