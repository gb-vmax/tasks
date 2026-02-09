# Bug Report

### Describe the bug

The `getModel()` function is returning the wrong model when looking up by type. It seems to be returning models that DON'T match the requested type instead of the ones that do match.

### Reproduction

```js
import { getModel } from './models';

// Try to get a specific model type
const requestModel = getModel('Request');

// Expected: Should return the Request model
// Actual: Returns a completely different model (or undefined if no non-matching models exist)
```

### Steps to reproduce
1. Call `getModel()` with a valid model type string (e.g., 'Request', 'Workspace', etc.)
2. Check what model is returned
3. The returned model is not the one you asked for

### Expected behavior

When calling `getModel('Request')`, it should return the model object where `m.type === 'Request'`. Instead it's returning models where the type does NOT match.

This is breaking model lookups throughout the application and causing various features to fail when they try to work with the wrong model type.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
