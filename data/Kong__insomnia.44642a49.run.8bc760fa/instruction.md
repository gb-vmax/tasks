# Bug Report

### Describe the bug

When using the JSONPath template tag with a filter that contains the `||` separator (for default values), the parsing logic doesn't correctly handle the separator. The function is attempting to split the filter string on `||` but appears to be defined outside of the `run` method scope, causing issues with how the filter is processed.

### Reproduction

```js
// Using JSONPath template tag with a default value
const filter = '$.user.name || default_name';

// The filter should be split into:
// - cleanFilter: '$.user.name'
// - defaultValue: 'default_name'

// But the parseFilterOptions function is not accessible within the run method
```

### Steps to reproduce:
1. Use a JSONPath template tag with a filter containing `||` for a default value
2. The filter parsing fails because `parseFilterOptions` is defined outside the proper scope
3. Template tag doesn't work as expected

### Expected behavior

The `parseFilterOptions` function should be accessible within the `run` method context so that filters with default values (using `||`) and array return syntax (using `[]`) can be properly parsed and processed.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
