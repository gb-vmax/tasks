# Bug Report

### Describe the bug
The `getOrCreate()` function in the settings model is not working correctly. When there's exactly one settings record in the database, it creates a duplicate instead of returning the existing one. This leads to multiple settings records being created unnecessarily.

### Reproduction
```js
// Initialize settings - creates first record
const settings1 = await getOrCreate();

// Call again - should return the same record but creates a new one
const settings2 = await getOrCreate();

// settings1 and settings2 have different IDs
console.log(settings1._id); // e.g., "settings_1"
console.log(settings2._id); // e.g., "settings_2" (should be "settings_1")
```

### Expected behavior
When a settings record already exists, `getOrCreate()` should return it instead of creating a new one. The function should only create a new settings record when none exists.

### Additional context
This appears to be causing issues where multiple settings records accumulate in the database over time, and the application may be reading from the wrong settings record depending on timing.

---
Repository: /testbed
