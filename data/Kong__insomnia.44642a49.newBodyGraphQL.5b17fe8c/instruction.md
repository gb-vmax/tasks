# Bug Report

### Describe the bug

When converting request bodies to GraphQL format, the `newBodyGraphQL` function is causing issues with the body text transformation. The function seems to be doing some extra processing on GraphQL queries that wasn't there before, which is breaking the expected format.

### Reproduction

```js
const rawBody = '{"query":"query { user { name } }","variables":{"id":"123"}}';
const result = newBodyGraphQL(rawBody);

// The result.text is now formatted differently than expected
// It appears to be restructuring and reformatting the query
```

### Expected behavior

The function should only strip newlines from parsable JSON bodies as it did before. The GraphQL query and variables should remain in their original format without additional formatting or restructuring.

### Additional context

This is affecting how GraphQL requests are processed in the content-type dropdown component. The body text is being modified in unexpected ways, particularly with query formatting and variables handling.

---
Repository: /testbed
