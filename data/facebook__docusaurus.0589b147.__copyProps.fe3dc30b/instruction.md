# Bug Report

### Describe the bug

After a recent update, module imports are not working correctly. When trying to import functions or objects from certain modules, I'm getting unexpected behavior where the imports appear to be undefined or empty objects.

### Reproduction

```js
import { someFunction } from 'some-module';

// someFunction is undefined even though it should be exported
console.log(someFunction); // undefined
```

This seems to affect modules that export both objects and functions. The issue wasn't present in the previous version.

### Expected behavior

Module exports should be properly copied and accessible when imported. All exported functions and objects should be available to the importing module.

### Additional context

This appears to be related to how properties are being enumerated and copied during the module bundling process. Regular object exports seem fine, but there's an issue with certain types of exports.

---
Repository: /testbed
