# Bug Report

### Describe the bug

The application fails to initialize properly due to a syntax error in the settings model. When trying to start the application or create new settings, it crashes immediately.

### Reproduction

```js
import { init } from './models/settings';

// This throws an error
const settings = init();
```

Or when trying to initialize with a profile:

```js
const settings = init('power-user');
```

### Expected behavior

The `init()` function should return a valid settings object with all default values properly merged with any environment or profile-specific overrides.

### System Info
- Node version: 18.x
- OS: macOS

This appears to have been introduced in a recent commit that added profile and environment override support. The application won't start at all now.

---
Repository: /testbed
