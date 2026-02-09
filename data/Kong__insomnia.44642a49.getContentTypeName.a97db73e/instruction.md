# Bug Report

### Describe the bug

The `getContentTypeName()` function is not returning the correct content type names. When I pass a valid content type string, it always returns an empty string instead of the expected content type name.

### Reproduction

```js
import { getContentTypeName } from './constants';

// This returns empty string but should return the content type name
const name = getContentTypeName('application/json');
console.log(name); // Expected: 'JSON', Actual: ''

// Same issue with other content types
const xmlName = getContentTypeName('text/xml');
console.log(xmlName); // Expected: 'XML', Actual: ''
```

Also noticed that when using the `useLong` parameter, the short name is returned instead of the long name and vice versa:

```js
const shortName = getContentTypeName('application/json', false);
const longName = getContentTypeName('application/json', true);
// The values seem to be swapped
```

### Expected behavior

- When passing a valid content type string like `'application/json'`, it should return the corresponding name (e.g., `'JSON'`)
- When `useLong` is `true`, it should return the long form of the name
- When `useLong` is `false`, it should return the short form of the name

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
