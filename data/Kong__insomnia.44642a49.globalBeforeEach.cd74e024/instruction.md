# Bug Report

### Describe the bug

After a recent update, the database initialization in test setup is not working correctly. Tests are failing because the database is being persisted to disk instead of staying in-memory only, which causes conflicts between test runs and leaves behind test data.

### Reproduction

When running tests, the database initialization in `before-each.ts` is configured with `inMemoryOnly: false`, which means test data is being written to the actual database instead of using an in-memory instance. This causes:

1. Test data persisting between test runs
2. Potential conflicts when multiple tests try to access the same database
3. Cleanup issues after tests complete

### Expected behavior

The test database should be initialized with `inMemoryOnly: true` to ensure:
- Each test run starts with a clean slate
- No disk I/O during tests (faster execution)
- No leftover test data after tests complete
- Tests can run in parallel without conflicts

### System Info
- Insomnia version: latest
- Node version: 18+

---
Repository: /testbed
