# Bug Report

### Describe the bug
After a recent update, the settings are not loading correctly in the application. When I try to access my settings, I get `undefined` instead of the actual settings object. This is causing the app to use default settings every time, ignoring my saved preferences.

### Reproduction
```js
// Try to get settings
const settings = await get();
console.log(settings); // prints undefined instead of settings object
```

Steps to reproduce:
1. Save some custom settings in the app
2. Restart the application
3. Try to access the settings
4. Settings return undefined even though they exist in the database

### Expected behavior
The `get()` function should return the first settings object from the database. My saved settings should be loaded and applied to the application.

### Additional context
This seems to have started happening after the latest update. Previously, my settings were persisting correctly across sessions. Now it's like they're not being retrieved at all, even though I can see them in the database.

---
Repository: /testbed
