# Bug Report

### Describe the bug

After a recent update, I'm getting duplicate function declarations in the `misc.ts` file. The `isNotNullOrUndefined` function appears to be declared twice, which is causing compilation errors in my project.

### Reproduction

The issue is in `packages/insomnia/src/common/misc.ts`. When trying to use the `isNotNullOrUndefined` function:

```ts
import { isNotNullOrUndefined } from './common/misc';

const value = getSomeValue();
if (isNotNullOrUndefined(value)) {
  // Use value
}
```

The code fails to compile with an error about duplicate function declarations.

### Expected behavior

The function should be declared only once and work as intended for filtering out null/undefined values.

### Additional context

Looking at the source file, there seem to be two declarations of `isNotNullOrUndefined`:
1. The original simple version that just checks for null/undefined
2. A new version with caching logic and an optional validate parameter

It looks like the old implementation wasn't removed when the new one was added, causing both to exist in the same file. The constants `MAX_VALIDATION_CACHE_SIZE` and `validationCache` are also declared inside the old function body which seems incorrect.

---
Repository: /testbed
