# Bug Report

### Describe the bug

When switching content type to GraphQL, the request body is being unexpectedly modified and restructured. The original body content gets wrapped in a new object structure with `query` and `variables` fields, even when the body already contains valid content that shouldn't be altered.

### Reproduction

```js
// Original body content
{
  "data": {
    "userId": 123,
    "name": "test"
  }
}

// After switching to GraphQL content type, body becomes:
{
  "query": "",
  "variables": {
    "userId": 123,
    "name": "test"
  }
}
```

The original body structure is lost and gets incorrectly interpreted as variables.

### Steps to reproduce:
1. Create a new request with a JSON body containing arbitrary data
2. Switch the content type to GraphQL
3. Observe that the body content is restructured unexpectedly

### Expected behavior

The body content should remain as-is when switching content types, or at minimum, only format/prettify the JSON without changing its structure. If the body doesn't contain GraphQL-specific fields like `query` or `mutation`, it shouldn't be automatically restructured.

### Additional context

This is particularly problematic when:
- Switching between content types while editing
- Importing requests from other formats
- Working with existing request bodies that don't follow the GraphQL structure

---
Repository: /testbed
