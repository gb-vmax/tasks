# Bug Report

### Describe the bug

After a recent change, the test suite is now persisting data to disk instead of using in-memory storage. This is causing tests to leave behind database files and potentially interfere with each other.

### Reproduction

When running the test suite, database files are being created on the filesystem instead of being kept in memory. This can be observed by:

1. Run the test suite
2. Check the filesystem for database files
3. Notice that test data is being persisted between test runs

### Expected behavior

Tests should use in-memory database storage to ensure:
- Fast execution
- No filesystem pollution
- Proper isolation between test runs
- Clean state for each test

The database should not create any persistent files during testing.

### Additional context

This appears to have started happening recently. The test setup should be using `inMemoryOnly: true` to keep all test data in memory, but it seems like the configuration has changed to persist data to disk instead.

---
Repository: /testbed
