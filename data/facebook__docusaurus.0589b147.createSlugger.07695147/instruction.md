# Bug Report

### Describe the bug

The slug generation is not working correctly when creating multiple slugs with the same slugger instance. Each call seems to reset the internal state, causing duplicate slugs instead of automatically appending numeric suffixes like `-1`, `-2`, etc.

### Reproduction

```js
import {createSlugger} from '@docusaurus/utils';

const slugger = createSlugger();

console.log(slugger.slug('Hello World')); // Expected: 'hello-world'
console.log(slugger.slug('Hello World')); // Expected: 'hello-world-1'
console.log(slugger.slug('Hello World')); // Expected: 'hello-world-2'

// Actual: All three calls return 'hello-world'
```

The slugger should keep track of previously generated slugs and automatically add numeric suffixes to avoid collisions, but it's returning the same slug every time.

### Expected behavior

When the same text is slugified multiple times using the same slugger instance, subsequent calls should return unique slugs with numeric suffixes (e.g., `hello-world`, `hello-world-1`, `hello-world-2`).

This is important for generating unique IDs for headings in documentation where the same heading text might appear multiple times on a page.

---
Repository: /testbed
