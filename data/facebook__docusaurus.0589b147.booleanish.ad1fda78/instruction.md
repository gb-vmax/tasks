# Bug Report

### Describe the bug

I'm experiencing an issue where the `booleanish` property type is not being exported correctly from the types module. It appears that `booleanish` is being mapped to the wrong implementation, which is causing unexpected behavior when working with HTML attributes that should accept boolean-ish values.

### Reproduction

```js
import { booleanish } from '@mdx-js/mdx'

// Trying to use booleanish for attribute validation
// Expected: booleanish type handler
// Actual: numberish type handler (wrong type)
```

When I try to access the `booleanish` export, I'm getting what appears to be a `numberish` type instead. This breaks attribute handling for properties that should accept boolean-like values (true/false/"true"/"false"/etc).

### Expected behavior

The `booleanish` export should return the correct booleanish type handler, not the numberish one. Attributes that are supposed to be boolean-ish should be processed correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like it might be a typo in the exports mapping? The module is exporting the wrong function for the `booleanish` key.

---
Repository: /testbed
