# Bug Report

### Describe the bug

The `settings.get()` function is returning `undefined` instead of the settings object. After investigating, it seems like the function is not properly retrieving the settings from the database.

### Reproduction

```js
import * as settings from './models/settings';

// Try to get settings
const result = await settings.get();
console.log(result); // Expected: settings object, Actual: undefined
```

### Steps to reproduce
1. Call `settings.get()` to retrieve settings
2. The function returns `undefined` even when settings exist in the database
3. Expected to return the first settings object from the database

### Expected behavior
The function should return the settings object from the database, not `undefined`.

### Additional context
This seems to have broken recently. The settings are definitely in the database but the get function isn't retrieving them properly anymore.

---
Repository: /testbed
