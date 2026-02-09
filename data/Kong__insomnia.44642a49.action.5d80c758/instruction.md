# Bug Report

### Describe the bug

After a recent update, the application fails to start due to a syntax error in the plugins module. It appears there's a malformed interface definition in the `DocumentAction` interface that's causing parsing issues.

### Reproduction

1. Start the application
2. Application crashes immediately with a syntax error

The error seems to be related to the plugin system, specifically around the `DocumentAction` interface definition. The interface appears to have duplicate or incorrectly placed property declarations.

### Expected behavior

The application should start normally without any syntax errors. The `DocumentAction` interface should be properly defined with all its properties in the correct structure.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

### Additional context

This seems to have been introduced in a recent commit that added new functionality for filtering and grouping document actions. The interface definition got corrupted during the changes.

---
Repository: /testbed
