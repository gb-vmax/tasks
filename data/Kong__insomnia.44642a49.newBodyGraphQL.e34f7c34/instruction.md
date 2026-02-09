# Bug Report

### Describe the bug

When converting a GraphQL request body, the content type dropdown is modifying the JSON structure in unexpected ways. Specifically, when the body contains additional properties beyond the standard GraphQL fields (`query`, `variables`, `operationName`), the order of properties in the JSON is being changed.

### Reproduction

```js
// Original GraphQL body with custom properties
const body = {
  customField: "value",
  query: "{ user { name } }",
  variables: {},
  anotherCustom: "test"
}

// After conversion, the property order changes:
// Expected: customField, query, variables, anotherCustom
// Actual: query, variables, customField, anotherCustom
```

Steps to reproduce:
1. Create a GraphQL request with a body that includes custom properties mixed with standard GraphQL fields
2. Convert the body using the content type dropdown
3. Notice that the JSON structure is reordered with GraphQL fields moved to the front

### Expected behavior

The JSON body should maintain its original property order. Custom fields should remain in their original positions relative to the standard GraphQL fields.

### Additional context

This appears to affect any GraphQL body that contains non-standard fields. The reordering might cause issues with APIs that expect a specific field order or with version control diffs showing unnecessary changes.

---
Repository: /testbed
