# Bug Report

### Describe the bug

The JSONPath template tag is broken after a recent update. When trying to use it in templates, it's not returning any results and seems to be causing parsing errors.

### Reproduction

```js
// Using the JSONPath template tag with a simple query
const jsonData = '{"users": [{"name": "Alice"}, {"name": "Bob"}]}';
const query = '$.users[0].name';

// Template: {% jsonpath jsonData query %}
// Expected: "Alice"
// Actual: No output or error
```

I've tried this with various JSONPath queries that were working before, including:
- Simple property access: `$.property`
- Array indexing: `$.items[0]`
- Nested objects: `$.user.profile.name`

All of them seem to fail now. The template just doesn't render anything.

### Expected behavior

The JSONPath template tag should query the JSON data and return the matching result like it did previously. For the example above, it should return `"Alice"`.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my workflow as I rely heavily on JSONPath queries in my request templates. Any help would be appreciated!

---
Repository: /testbed
