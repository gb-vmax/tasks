# Bug Report

### Describe the bug
Query parameters with type annotations and disabled state are not being parsed correctly. When parsing URL query strings that contain parameters with `::type` suffixes or keys prefixed with `#` (to indicate disabled state), the parser is not extracting and preserving this metadata.

### Reproduction
```js
const queryStr = 'key1=value1&key2=value2::string&#key3=value3';
const parsed = QueryParam.parse(queryStr);

// Expected: parsed parameters should include type and disabled metadata
// Actual: type and disabled information is lost during parsing
console.log(parsed);
// Currently returns: [{ key: 'key1', value: 'value1' }, { key: 'key2', value: 'value2::string' }, { key: '#key3', value: 'value3' }]
// Should return: [{ key: 'key1', value: 'value1' }, { key: 'key2', value: 'value2', type: 'string' }, { key: 'key3', value: 'value3', disabled: true }]
```

### Expected behavior
- Parameters with keys starting with `#` should be marked as `disabled: true` and the `#` should be stripped from the key
- Parameters with values containing `::type` should have the type extracted into a separate `type` field
- The type annotation should be removed from the actual value

### Additional context
This is affecting our ability to properly handle query parameters that have type information or disabled states encoded in the URL string. The current parser just returns the raw key/value pairs without extracting this metadata.

---
Repository: /testbed
