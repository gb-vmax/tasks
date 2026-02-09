# Bug Report

### Describe the bug
The `get()` function in the settings model is returning the wrong settings object. After a recent change, it appears to be attempting to access index `[1]` on what is now an object (changed from an array), which will always return `undefined`.

### Reproduction
```js
import { get } from './models/settings';

// Try to retrieve settings
const settings = await get();

// settings is undefined instead of the actual settings object
console.log(settings); // undefined
```

### Expected behavior
The `get()` function should return the first (and typically only) settings object from the database query results. Currently it's returning `undefined` because:
1. The results are now being initialized as an object `{}` instead of an array `[]`
2. It's trying to access index `[1]` instead of `[0]`

This breaks any functionality that relies on retrieving application settings.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
