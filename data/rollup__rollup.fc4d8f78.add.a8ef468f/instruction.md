# Bug Report

### Describe the bug

The warning system seems to be handling deferred and immediate warnings incorrectly. Warnings that should be displayed immediately are being deferred, and warnings that should be deferred are being shown immediately instead.

### Reproduction

When running rollup with various warning codes, the output behavior is reversed:

```js
// Warnings with codes that should trigger immediate handlers
// are being collected and deferred instead

// Warnings with codes that should be deferred
// are being handled immediately
```

For example, if you have a warning that's supposed to be shown right away (like certain plugin warnings), it gets queued up instead. And warnings that should be batched together at the end are being printed out one by one as they occur.

### Expected behavior

- Warnings registered in `immediateHandlers` should be displayed immediately when they occur
- Warnings registered in `deferredHandlers` should be collected and displayed later in batch
- The warning count should increment regardless of the `silent` flag setting

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
