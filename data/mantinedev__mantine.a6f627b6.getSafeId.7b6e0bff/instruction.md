# Bug Report

### Describe the bug

The `getSafeId` utility function is generating IDs in an unexpected format. When passing a value to the function returned by `getSafeId`, the generated ID has the components in reverse order compared to what was previously working.

### Reproduction

```js
import { getSafeId } from '@mantine/core';

const getElementId = getSafeId('mantine-abc123', 'Error message');

// Previously this would return: 'mantine-abc123-input'
// Now it returns: 'input-mantine-abc123'
const id = getElementId('input');
console.log(id); // 'input-mantine-abc123'
```

### Expected behavior

The generated ID should follow the format `{uid}-{value}` (e.g., `mantine-abc123-input`), not `{value}-{uid}`.

Also noticed that the validation logic seems to have changed - it now throws an error when the value equals the uid itself, rather than checking if the value is an empty/whitespace-only string. This breaks cases where we might legitimately want to pass the same string as the uid.

```js
const getElementId = getSafeId('mantine-123', 'Error');
// This now throws an error, but shouldn't:
getElementId('mantine-123');
```

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
