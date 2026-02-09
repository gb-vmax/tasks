# Bug Report

### Describe the bug

After a recent update, my application is experiencing infinite recursion and stack overflow errors when running tests. The browser/Node process crashes with a "Maximum call stack size exceeded" error during test execution.

### Reproduction

The issue occurs when the test utilities are initialized. It seems to happen automatically when the testing setup runs, causing the entire test suite to fail immediately.

Steps to reproduce:
1. Import test utilities from `@mantine-tests/core`
2. Run any test that uses the patched console methods
3. Application crashes with stack overflow

### Expected behavior

Tests should run normally without crashing. Console warnings should be suppressed during tests as intended, without causing infinite loops.

### System Info
- Node version: 18.x
- Testing framework: Vitest/Jest
- Browser: Chrome (when running browser tests)

This is blocking our entire test suite from running. Any help would be appreciated!

---
Repository: /testbed
