# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with proto file retrieval in Insomnia. When I create or update a proto file, subsequent calls to retrieve proto files by parent ID are returning stale/cached data instead of the latest values from the database.

### Reproduction

1. Create a proto file with a specific parent ID
2. Immediately query for proto files by that parent ID
3. Update the proto file (e.g., change its name or content)
4. Query again for proto files by the same parent ID
5. The query returns the old cached version instead of the updated data

This seems to be related to some caching mechanism that was recently added. The cache appears to be storing results but not properly invalidating when the underlying data changes.

### Expected behavior

When proto files are created, updated, or removed, any subsequent queries should return the current state from the database, not cached values. The cache should either be invalidated properly or the retrieval functions should use the cache correctly.

### Additional context

This is causing issues in our workflow where we need to see proto file changes immediately. It seems like there might be a mismatch between the caching layer and the actual database operations.

---
Repository: /testbed
