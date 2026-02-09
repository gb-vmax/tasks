# Bug Report

### Describe the bug

When trying to create a new Proto Directory, the application crashes or returns undefined instead of creating a properly initialized directory object. This seems to affect any workflow that involves creating new proto directories.

### Reproduction

```js
import { init } from './proto-directory';

// Attempting to initialize a new proto directory
const newProtoDir = init();

console.log(newProtoDir); // Returns undefined instead of an object
```

### Expected behavior

The `init()` function should return a new proto directory object with default values:
```js
{
  name: 'New Proto Directory'
}
```

Instead, it returns `undefined` which breaks any code that depends on this initialization.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
