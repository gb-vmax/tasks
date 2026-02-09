# Bug Report

### Describe the bug

When using the `find` method with pagination options (`$limit` and `$skip`) in the query object, the pagination parameters are being passed directly to NeDB which doesn't recognize them. This causes the query to fail or return unexpected results since NeDB doesn't understand these custom pagination fields.

### Reproduction

```js
// Try to find documents with pagination
const results = await database.find('requests', {
  parentId: 'wrk_123',
  $limit: 10,
  $skip: 5
});

// The query fails because NeDB doesn't recognize $limit and $skip
// These fields should be extracted and applied using NeDB's .limit() and .skip() methods
```

### Expected behavior

The `find` method should properly extract `$limit` and `$skip` from the query object and apply them using NeDB's cursor methods (`.limit()` and `.skip()`) rather than passing them as part of the query criteria. This would allow for proper pagination support.

### Additional context

Currently trying to implement pagination for request history but the database layer doesn't support it properly. Would be great if we could pass pagination options directly in the query object like:

```js
database.find('requests', { 
  parentId: 'wrk_123',
  $limit: 20,
  $skip: 0
})
```

---
Repository: /testbed
