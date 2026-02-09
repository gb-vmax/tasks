# Bug Report

### Describe the bug

The `randomId` utility function is generating IDs with unexpected characters. I'm seeing digits and letters from 0-9 and a-f in the generated IDs, but I was expecting the usual alphanumeric format (0-9, a-z) that this function typically produces.

### Reproduction

```js
import { randomId } from '@mantine/hooks';

// Generate a few IDs
console.log(randomId()); // e.g., "mantine-a3f4e5d6c"
console.log(randomId()); // e.g., "mantine-1b2c3d4e5"
console.log(randomId('test-')); // e.g., "test-9f8e7d6c5"
```

The generated IDs now contain hex characters (0-9, a-f) instead of the expected base-36 alphanumeric characters (0-9, a-z).

### Expected behavior

The function should generate random IDs using base-36 encoding (0-9 and a-z characters), not base-16 (hex). The IDs should look like `mantine-x7k2m9p3q` rather than `mantine-a3f4e5d6c`.

### System Info
- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
