# Bug Report

### Describe the bug
When working with snapshot state entries, the `key` property is not being returned correctly. Instead of getting the expected string value 'key', the function is returning another function rather than executing it and returning its result.

### Reproduction
```js
import { snapshotStateEntrySchema } from './type-schemas';

const schema = snapshotStateEntrySchema;
const keyValue = schema.key();

console.log(keyValue); // Expected: 'key', Actual: [Function]
console.log(typeof keyValue); // Returns 'function' instead of 'string'
```

### Expected behavior
The `key` property should return the string `'key'` directly, matching the behavior of the `blob` and `name` properties in the same schema.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
