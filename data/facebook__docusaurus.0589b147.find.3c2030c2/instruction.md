# Bug Report

### Describe the bug

I'm encountering an issue with data attribute handling when working with HTML attributes. It seems like data attributes with dashes (like `data-test-value`) are not being processed correctly.

### Reproduction

```js
// When trying to work with data attributes that have dashes
const element = {
  'data-test-value': 'hello'
}

// The attribute name gets mangled incorrectly
// Expected: dataTestValue
// Actual: data-estValue (missing the 't')
```

### Expected behavior

Data attributes with dashes should be properly converted to camelCase format. For example:
- `data-test-value` should become `dataTestValue`
- `data-my-attr` should become `dataMyAttr`

Currently it appears that the first character after `data-` is being dropped during the conversion process.

### System Info
- Version: 10.0.0
- Node: v18.x

---
Repository: /testbed
