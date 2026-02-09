# Bug Report

### Describe the bug

After a recent update, the test database configuration seems to have changed and is now persisting data between test runs instead of using an in-memory only database. This is causing tests to interfere with each other and leading to flaky test behavior.

### Reproduction

1. Run any test suite that uses the database
2. Run the same tests again
3. Notice that data from the previous test run is still present
4. Tests that expect a clean database state fail or behave unexpectedly

### Expected behavior

The test database should be configured to use `inMemoryOnly: true` to ensure each test run starts with a clean slate and tests don't interfere with each other. Data should not persist between test runs.

### Additional context

This appears to affect all tests that rely on the database initialization in the `globalBeforeEach` setup. The database configuration should be ephemeral for testing purposes to maintain test isolation.

---
Repository: /testbed
