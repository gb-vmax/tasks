# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with plugin hooks timing out unexpectedly. The application seems to be rejecting plugin executions with timeout errors even when the plugins are working normally.

### Reproduction

When using a custom plugin with request hooks:

1. Create a plugin with a request hook that performs some async operation
2. The hook executes normally and completes within a reasonable time
3. Application throws an error about the plugin exceeding timeout

The error message indicates the plugin exceeded a 30 second timeout, but this happens even when the plugin completes much faster.

### Expected behavior

Plugin hooks should execute successfully without timeout errors when they complete within the allowed time limit. The timeout mechanism should only trigger when plugins actually take too long to execute.

### Additional context

This appears to have started happening recently. Previously, plugins were working fine without any timeout-related errors. The issue seems to affect all plugins that use request hooks, regardless of their actual execution time.

---
Repository: /testbed
