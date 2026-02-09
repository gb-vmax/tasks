# Bug Report

### Describe the bug

After a recent update, the `Header` class seems to have lost most of its functionality. When trying to create or parse headers, I'm getting errors about missing methods and the constructor not working properly.

### Reproduction

```js
// This used to work but now fails
const header = new Header({ key: 'Content-Type', value: 'application/json' });

// Parsing headers also broken
const headers = Header.parse('Content-Type: application/json\nUser-Agent: MyApp/1.0');

// Static create method not working
const newHeader = Header.create({ key: 'Authorization', value: 'Bearer token' });
```

### Expected behavior

The Header class should be able to:
- Create new header instances via constructor
- Parse header strings into header objects
- Use the static `create()` method to instantiate headers
- Convert headers back to strings with `unparse()`

All of these operations were working fine before but now seem to be completely broken or missing.

### System Info
- Package: insomnia-sdk
- Node version: 18.x

---
Repository: /testbed
