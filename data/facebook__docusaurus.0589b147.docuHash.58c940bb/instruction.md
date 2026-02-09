# Bug Report

### Describe the bug

The `docuHash` function is generating incorrect hashes for the root path `/`. After a recent change, when passing `/` as input, the function returns a hash like `index-xxx` instead of just `index`. This breaks routing and file generation for the root/home page.

### Reproduction

```js
import { docuHash } from '@docusaurus/utils';

// This now returns something like "index-a1b" instead of "index"
const hash = docuHash('/');
console.log(hash); // Expected: "index", Actual: "index-a1b"
```

### Expected behavior

When `docuHash('/')` is called, it should return `'index'` without any hash suffix, as the root path is a special case that should have a predictable, clean filename.

### Additional context

This seems to have started happening recently. The root path should be handled specially to ensure consistent file naming for the home page across builds.

---
Repository: /testbed
