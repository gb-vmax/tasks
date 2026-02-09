# Bug Report

### Describe the bug

I'm experiencing an issue with template rendering where properties starting with an underscore are not being processed correctly. It seems like the logic for determining whether to track paths for underscore-prefixed properties has been inverted.

### Reproduction

```js
const data = {
  _privateField: '{{ someVariable }}',
  publicField: '{{ anotherVariable }}'
}

// When rendering with first=true
const result = await render(data, context, { first: true })

// Expected: _privateField should be rendered without path tracking
// Actual: _privateField is being rendered WITH path tracking
// This causes incorrect behavior in the rendering pipeline
```

### Expected behavior

When `first` is true, properties starting with underscore should be rendered without path tracking (using `next(x[key], path)` directly). Properties not starting with underscore should include the path prefix.

Currently it appears to be doing the opposite - underscore properties are getting path tracking when they shouldn't.

### System Info
- Version: Latest from main branch
- This affects template variable rendering in requests

---
Repository: /testbed
