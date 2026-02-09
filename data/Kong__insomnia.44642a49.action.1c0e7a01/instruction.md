# Bug Report

### Describe the bug

Getting a syntax error when trying to load plugins. The application fails to start and shows a compilation error related to the plugin system.

### Reproduction

1. Start the application with any plugin that defines a `DocumentAction`
2. Application fails to load with a syntax error

The error appears to be related to the `DocumentAction` interface definition in the plugin system. It looks like there's a duplicate interface declaration or malformed TypeScript code.

### Expected behavior

The application should start normally and plugins should load without any syntax errors. The `DocumentAction` interface should be properly defined with all its properties (action, label, icon, hideAfterClick, when, group).

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
