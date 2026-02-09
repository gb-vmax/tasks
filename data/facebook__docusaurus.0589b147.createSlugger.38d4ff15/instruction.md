# Bug Report

### Describe the bug

The `createSlugger()` function is not respecting the `maintainCase` option correctly. When I pass `maintainCase: true`, the slugger still converts everything to lowercase, and when I pass `maintainCase: false` (or don't pass it at all), it maintains the case instead of lowercasing.

### Reproduction

```js
import { createSlugger } from '@docusaurus/utils';

const slugger = createSlugger();

// Expected: "hello-world" (lowercase)
// Actual: "Hello-World" (case maintained)
console.log(slugger.slug('Hello World'));

// Expected: "Hello-World" (case maintained)
// Actual: "hello-world" (lowercase)
console.log(slugger.slug('Hello World', { maintainCase: true }));
```

The behavior seems to be inverted - when I want to maintain case, it lowercases, and when I want lowercase (the default), it maintains case.

### Expected behavior

- By default (no options), slugs should be lowercased
- When `maintainCase: true` is passed, the original casing should be preserved
- When `maintainCase: false` is explicitly passed, slugs should be lowercased

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
