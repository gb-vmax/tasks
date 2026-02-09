# Bug Report

### Describe the bug

The application fails to start after a recent update. There seems to be a syntax error in the error modal component that's preventing the app from loading properly.

### Reproduction

1. Start the application
2. Application crashes immediately on load

The error appears to be related to the ErrorModal component - looks like there's duplicate code or malformed syntax in the `useImperativeHandle` hook implementation.

### Expected behavior

The application should start normally without any syntax errors.

### Additional context

This started happening after the latest changes to the error modal. The component seems to have some duplicated code blocks that are causing parsing issues. Specifically, the `show` method appears to be defined multiple times within the `useImperativeHandle` hook, and there's also an interface definition (`ErrorHistoryEntry`) placed in an invalid location inside the hook definition.

---
Repository: /testbed
