# Bug Report

### Describe the bug

The `getById` function in the proto-file model is returning an array instead of a single object. This breaks any code that expects to work with a single ProtoFile object directly.

### Reproduction

```js
import * as protoFile from './models/proto-file';

// Assuming we have a proto file with id 'test-id'
const result = protoFile.getById('test-id');

// This now fails because result is an array
console.log(result.name); // undefined
console.log(result._id);  // undefined

// Need to access the first element instead
console.log(result[0].name); // Works but shouldn't be necessary
```

### Expected behavior

`getById` should return a single ProtoFile object (or null/undefined if not found), not wrapped in an array. All other similar getter functions in the codebase return single objects, so this is inconsistent.

### Additional context

This seems to have broken after a recent change. Any code that calls `getById` and tries to access properties directly will fail since it's now receiving an array instead of the object itself.

---
Repository: /testbed
