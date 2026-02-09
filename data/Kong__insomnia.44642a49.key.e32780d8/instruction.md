# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the request SDK. The code appears to be corrupted or truncated in the `request.ts` file. Methods like `_postman_propertyAllowsMultipleValues()`, `_postman_propertyIndexKey()`, `toJSON()`, and `toString()` are missing their `static` and `override` keywords, and some method implementations appear to be cut off mid-line.

### Reproduction

```js
import { FormParam } from '@insomnia/sdk';

const param = new FormParam({
  key: 'username',
  value: 'test'
});

// Trying to call toString() results in errors
const paramString = param.toString();
```

The code fails to parse/compile due to malformed method declarations in the FormParam class.

### Expected behavior

The FormParam class should have properly formatted method declarations with correct keywords (`static`, `override`) and complete implementations. Methods like `toString()` should return properly encoded key-value pairs.

### System Info
- Package: @insomnia/sdk
- Node version: 18.x

---
Repository: /testbed
