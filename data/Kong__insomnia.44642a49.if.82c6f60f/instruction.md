# Bug Report

### Describe the bug

After a recent update, JSON prettification is completely broken. When trying to format JSON strings, the output becomes corrupted and the function appears to hang or produce invalid results.

### Reproduction

```js
import { jsonPrettify } from './utils/prettify/json';

const json = '{"user":{"name":"test","active":true}}';
const result = jsonPrettify(json);

console.log(result);
// Expected: properly formatted JSON with indentation
// Actual: corrupted or malformed output
```

Also happens with nested strings:

```js
const jsonWithStrings = '{"message":"Hello \\"World\\"","status":"ok"}';
const formatted = jsonPrettify(jsonWithStrings);
// Output is incorrect
```

### Expected behavior

The `jsonPrettify` function should properly format JSON strings with correct indentation and preserve escaped characters within string values. Nested objects and strings with escape sequences should be handled correctly.

### Additional context

This seems to have broken string handling inside JSON objects. The prettifier used to work fine with escaped quotes and other special characters but now something is off with the state machine logic.

---
Repository: /testbed
