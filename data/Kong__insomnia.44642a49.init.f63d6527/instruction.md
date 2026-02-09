# Bug Report

### Describe the bug
When trying to create a new proto directory using the `init()` function, the application crashes or behaves unexpectedly. It seems like the function is not returning the expected object structure anymore.

### Reproduction
```js
import { init } from './proto-directory';

// Try to create a new proto directory
const newDirectory = init();

// This should work but doesn't
console.log(newDirectory); // undefined or causes error
```

### Expected behavior
The `init()` function should return a valid proto directory object with the default name 'New Proto Directory' that can be used to create new proto directories in the application.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
