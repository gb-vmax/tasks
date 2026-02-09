# Bug Report

### Describe the bug

After a recent update, I'm experiencing performance issues when working with gRPC requests. The application seems to be making unnecessary database updates every time I access request metadata, even when just reading data. This is causing noticeable slowdowns, especially when switching between requests or loading request lists.

### Reproduction

```js
// Just retrieving metadata now triggers updates
const meta = await getByParentId(requestId);
// This should be a simple read operation but appears to be writing to DB

// When rapidly switching between requests, each access updates the database
for (let i = 0; i < 10; i++) {
  await getByParentId(requestId); // Each call seems to trigger a write
}
```

### Expected behavior

Reading request metadata should not trigger database writes unless explicitly updating data. The `getByParentId` function should only retrieve existing data without side effects. Updates to `lastActive` or other tracking fields should happen through explicit update calls, not during read operations.

### Additional context

This seems to have started after changes to the grpc-request-meta model. The function appears to be automatically updating timestamps on every read, which wasn't the case before. This creates unnecessary database load and impacts performance when working with multiple requests.

---
Repository: /testbed
