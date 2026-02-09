# Bug Report

### Describe the bug

I'm encountering an issue where warnings about calling namespaces are not being logged correctly when using tagged template expressions. It seems like the warning system isn't triggering when it should.

### Reproduction

```js
import * as myNamespace from './module';

// This should trigger a warning but doesn't
myNamespace`template string`;
```

When trying to use a namespace as a tag function in a tagged template expression, I expect to see a warning logged (since you can't call a namespace), but no warning appears.

### Expected behavior

A warning should be logged when attempting to use a namespace as a tag function in a tagged template expression, similar to how it works for regular function calls.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
