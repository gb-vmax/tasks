# Bug Report

### Describe the bug

The `filterHeaders` function appears to have duplicate code after a recent change. When trying to filter headers, the function seems to have both the new wildcard matching logic and the old filtering code, which causes unexpected behavior. The function returns early with an empty array in some cases, but then has unreachable code that tries to do the original filtering.

### Reproduction

```js
import { filterHeaders } from './misc';

const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token' },
  { name: 'X-Custom-Header', value: 'test' }
];

// Try to filter headers
const result = filterHeaders(headers, 'Content-Type');
console.log(result); // Returns empty array or unexpected results
```

### Expected behavior

The function should properly filter headers based on the provided name pattern. With the wildcard support added, it should:
- Match exact header names when no wildcard is used
- Support prefix matching with `prefix*`
- Support suffix matching with `*suffix`
- Support contains matching with `*middle*`
- Support array of patterns

However, there seems to be dead code after the return statement that never gets executed.

### System Info
- Version: Latest from main branch
- The issue appeared after the wildcard pattern matching feature was added

---
Repository: /testbed
