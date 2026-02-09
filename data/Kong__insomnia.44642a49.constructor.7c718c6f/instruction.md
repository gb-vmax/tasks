# Bug Report

### Describe the bug

After a recent update, the Header class seems to be completely broken. The entire class implementation has been replaced with just a single static method `normalizeHeaderKey()`, and all the core functionality is gone.

### Reproduction

```js
// This used to work but now fails
const header = new Header({ key: 'content-type', value: 'application/json' });

// These methods are no longer available
Header.create({ key: 'Authorization', value: 'Bearer token' });
Header.parse('Content-Type: application/json\nUser-Agent: MyClient/1.0');
Header.unparse(headers);
```

### Expected behavior

The Header class should have:
- A constructor that accepts HeaderDefinition or string
- Static methods like `create()`, `parse()`, `parseSingle()`, `unparse()`, and `unparseSingle()`
- Properties like `key`, `value`, `id`, `name`, `type`, and `disabled`
- The ability to create and manipulate HTTP headers

Instead, all of these are missing and only `normalizeHeaderKey()` remains.

### System Info
- Package: insomnia-sdk
- File: packages/insomnia-sdk/src/objects/headers.ts

This looks like the file got accidentally truncated or only partially updated. The entire class implementation is gone!

---
Repository: /testbed
