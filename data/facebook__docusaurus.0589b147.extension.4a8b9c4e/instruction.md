# Bug Report

### Describe the bug

I'm experiencing strange behavior when combining multiple MDX extensions. It seems like the order of extension processing has been reversed, and there's also an issue with `enter`/`exit` handlers being swapped.

### Reproduction

When I register multiple extensions with handlers, the execution order is backwards from what I expect:

```js
const extension1 = {
  canContainEols: ['customBlock'],
  transforms: [transform1],
  enter: { customNode: enterHandler1 }
}

const extension2 = {
  canContainEols: ['anotherBlock'],
  transforms: [transform2],
  exit: { customNode: exitHandler2 }
}

// After combining extensions
const combined = combineExtensions([extension1, extension2])
```

What happens:
1. The `canContainEols` array has items in reverse order (extension2's items appear first)
2. The `transforms` array is also reversed
3. Most concerning: `enter` handlers seem to be registered as `exit` handlers and vice versa

This is causing my custom syntax extensions to fail because the handlers run in the wrong order and the enter/exit lifecycle is completely broken.

### Expected behavior

- Extensions should be combined in the order they're provided
- `enter` handlers should remain as `enter` handlers
- `exit` handlers should remain as `exit` handlers
- The order of `canContainEols` and `transforms` should be preserved

### Additional context

This appears to have started happening recently. The extension combination logic seems to have been modified, but the changes break existing extension code that relies on proper handler registration and execution order.

---
Repository: /testbed
