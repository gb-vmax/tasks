# Bug Report

### Describe the bug

The `logger.throwError()` function is not actually throwing errors anymore. When I call it, the function executes without raising an exception, which breaks error handling in my application.

### Reproduction

```js
import logger from '@docusaurus/logger';

try {
  logger.throwError('Something went wrong');
  console.log('This should not be reached');
} catch (error) {
  console.log('Error caught:', error.message);
}
```

### Expected behavior

The code should throw an error and enter the catch block. Instead, it just continues execution and prints "This should not be reached".

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking my build scripts that rely on proper error handling. Any help would be appreciated!

---
Repository: /testbed
