# Bug Report

### Describe the bug

JSX attributes are not being transformed correctly when using `jsxMode: 'classic'` or `jsxMode: 'automatic'`. The attributes remain in JSX syntax instead of being converted to the expected object property format.

### Reproduction

```js
// Input JSX with jsxMode: 'classic'
<div className="test" data-id="123" />

// Expected output: attributes converted to object properties
// className: "test", "data-id": "123"

// Actual output: attributes remain unchanged in JSX format
```

When compiling JSX with either `classic` or `automatic` mode, the attribute transformation is skipped entirely. This affects:
- Simple attributes like `className="value"`
- Attributes with boolean values like `disabled`
- Attributes with namespaces like `xml:lang="en"`
- Attributes with multiline string values

### Expected behavior

JSX attributes should be transformed into object property syntax when using `jsxMode: 'classic'` or `jsxMode: 'automatic'`. For example:
- `foo="bar"` should become `foo: "bar"`
- `disabled` should become `disabled: true`
- Keys that need escaping should be properly quoted

### System Info

- Rollup version: latest
- JSX mode: classic/automatic

---
Repository: /testbed
