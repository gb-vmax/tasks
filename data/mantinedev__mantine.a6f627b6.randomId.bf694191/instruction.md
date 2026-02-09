# Bug Report

### Describe the bug

The `randomId` utility function is generating IDs with unexpected characters. After a recent update, the generated IDs now contain hexadecimal characters (0-9, a-f) instead of the base-36 alphanumeric characters (0-9, a-z) that were previously used.

### Reproduction

```js
import { randomId } from '@mantine/hooks';

// Generate a few IDs
const id1 = randomId();
const id2 = randomId('custom-');
const id3 = randomId();

console.log(id1); // e.g., "mantine-0.a3f8b2d"
console.log(id2); // e.g., "custom-0.c4e9a1b"
console.log(id3); // e.g., "mantine-0.f2d8c3a"
```

### Expected behavior

The IDs should be generated using base-36 encoding (0-9, a-z), which provides better readability and a larger character set. The current implementation uses base-16 (hexadecimal), which limits the available characters and changes the format of generated IDs.

Previously generated IDs would look like: `mantine-k2j8x9p5q` (using letters beyond 'f')
Now they look like: `mantine-0.a3f8b` (only using 0-9, a-f)

This is breaking for applications that may have validation or expectations around the ID format.

### System Info

- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
