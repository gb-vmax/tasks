# Bug Report

### Describe the bug

When passing an empty string or whitespace-only string as a URL to `toUrlObject()`, the function doesn't throw an error as expected. The function appears to have been modified to normalize and validate URLs, but empty/whitespace strings are now being processed instead of being rejected immediately.

### Reproduction

```js
import { toUrlObject } from './objects/urls';

// This should throw an error but doesn't
const result1 = toUrlObject('');

// This should also throw an error but doesn't  
const result2 = toUrlObject('   ');
```

### Expected behavior

The function should throw an error with message "Request URL is not specified" when given an empty or whitespace-only string, similar to how it handled falsy values before.

### Additional context

This seems to have started after some changes to the URL handling logic. The original validation that checked `if (!url)` appears to have been replaced with more complex normalization logic, but the edge case of empty strings isn't being handled properly anymore.

---
Repository: /testbed
