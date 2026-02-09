# Bug Report

### Describe the bug

I'm encountering an issue with directive attribute parsing where attribute values are not being assigned correctly. It seems like the attribute values are either missing or being placed in the wrong location in the attributes list.

### Reproduction

```js
// Parse a directive with attributes
const input = ':directive[text]{key="value"}';

// After parsing, the attribute value is not correctly associated with the key
// The attributes list appears to have undefined or incorrectly indexed values
```

When parsing directives with attributes, the key-value pairs are not being stored properly. The value appears to be written to an invalid index in the attributes array, causing the parsed attributes to be incomplete or incorrect.

### Expected behavior

Directive attributes should be parsed correctly with their values properly associated with their keys. For example, `{key="value"}` should result in an attribute entry where the key maps to "value".

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
