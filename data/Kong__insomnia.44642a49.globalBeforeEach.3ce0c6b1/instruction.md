# Bug Report

### Describe the bug

After a recent update, the test database is now persisting to disk instead of running in memory only. This is causing issues with test isolation and cleanup - tests are leaving behind database files and subsequent test runs are picking up stale data from previous runs.

### Reproduction

Run the test suite multiple times in succession. You'll notice:
1. Database files are being created in the file system
2. Tests that should start with a clean state are seeing data from previous test runs
3. Test cleanup is incomplete, leaving artifacts behind

This is affecting test reliability and causing intermittent failures that are hard to debug.

### Expected behavior

Tests should use an in-memory database that doesn't persist to disk. Each test run should start with a completely clean state, and no database files should be created or left behind after tests complete.

### Additional context

This seems to have started happening recently. The test setup used to properly initialize with `inMemoryOnly: true` but something changed in the database initialization logic.

---
Repository: /testbed
