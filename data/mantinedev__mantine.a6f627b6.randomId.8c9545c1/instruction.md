# Bug Report

### Describe the bug

The `randomId` utility function is generating IDs with unexpected characters. After a recent update, the generated IDs now contain only numeric digits instead of the alphanumeric characters they used to produce.

### Reproduction

```js
import { randomId } from '@mantine/hooks';

// Generate a few IDs
console.log(randomId());
console.log(randomId('custom-'));
console.log(randomId());

// Output now looks like:
// mantine-1234567
// custom-8901234
// mantine-5678901

// But it used to produce alphanumeric strings like:
// mantine-k2j5h8x9a
// custom-p9m4n7q2b
// mantine-r3t6y8u1e
```

### Expected behavior

The `randomId` function should generate random IDs containing alphanumeric characters (0-9, a-z) to ensure better uniqueness and collision avoidance. The current numeric-only output significantly reduces the entropy of generated IDs.

### System Info
- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
