# Bug Report

### Describe the bug

The `randomId()` utility function is generating IDs with unexpected characters. I'm seeing numbers like `0-9` in the generated IDs, but also getting strange characters that don't seem to be valid alphanumeric characters from base-36.

### Reproduction

```js
import { randomId } from '@mantine/hooks';

// Generate a few IDs
console.log(randomId()); // Expected: mantine-xyz123abc
console.log(randomId('custom-')); // Expected: custom-abc456def

// The generated IDs sometimes contain invalid characters
// or have unexpected format
```

When I generate multiple IDs, some of them look correct but others have characters that shouldn't be there for a base-36 encoded string.

### Expected behavior

The `randomId()` function should consistently generate valid random IDs using alphanumeric characters (0-9, a-z) from base-36 encoding. The IDs should be properly formatted with the prefix followed by a random alphanumeric string.

### System Info

- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
