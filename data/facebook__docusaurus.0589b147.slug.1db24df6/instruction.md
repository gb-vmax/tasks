# Bug Report

### Describe the bug

The `createSlugger()` function is generating slugs with incorrect casing behavior. When I explicitly set `maintainCase: true` in the options, the slugs are being converted to lowercase instead of preserving the original case. Conversely, when I set `maintainCase: false` or don't provide the option at all, the case is being maintained when it should be lowercased.

### Reproduction

```js
import { createSlugger } from '@docusaurus/utils';

const slugger = createSlugger();

// This should maintain case but gets lowercased
const slug1 = slugger.slug('Hello World', { maintainCase: true });
console.log(slug1); // Expected: 'Hello-World', Actual: 'hello-world'

// This should be lowercased but maintains case
const slug2 = slugger.slug('Hello World', { maintainCase: false });
console.log(slug2); // Expected: 'hello-world', Actual: 'Hello-World'

// Default behavior (no options) should lowercase
const slug3 = slugger.slug('Hello World');
console.log(slug3); // Expected: 'hello-world', Actual: 'Hello-World'
```

### Expected behavior

- When `maintainCase: true` is passed, the original casing should be preserved in the slug
- When `maintainCase: false` is passed or no options are provided, the slug should be lowercased
- The behavior should match what's documented for the `maintainCase` option

### System Info

- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
