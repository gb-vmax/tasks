# Bug Report

### Describe the bug

After a recent update, the plugin API's `app.getInfo()` method is returning additional properties that weren't there before. This is breaking our plugin's logic which was expecting only `version` and `platform` fields.

### Reproduction

```js
const appContext = insomnia.app;
const info = appContext.getInfo();

// Previously returned: { version: '...', platform: '...' }
// Now returns: { version: '...', platform: '...', memory: {...}, runtime: {...}, renderPurpose: '...', capabilities: {...} }

// Our code that checks the object keys is now failing
const expectedKeys = ['version', 'platform'];
const actualKeys = Object.keys(info);
// actualKeys now includes 'memory', 'runtime', 'renderPurpose', 'capabilities'
```

### Expected behavior

The `getInfo()` method should maintain backward compatibility and only return the documented fields (`version` and `platform`), or at least the additional fields should be opt-in or documented as part of the API contract.

Our plugin code was relying on the stable shape of this object for serialization and comparison purposes, and the unexpected additional properties are causing issues.

### System Info
- Insomnia version: latest
- Plugin API context: app

---
Repository: /testbed
