# Bug Report

### Describe the bug

After a recent update, the app crashes when trying to show a prompt dialog. The application fails to start and throws a syntax error related to the prompt functionality in the plugin context.

### Reproduction

1. Start the application
2. Trigger any plugin that uses `app.prompt()` 
3. Application crashes immediately

The issue seems to be in the prompt handling code. Looking at the code, there appears to be malformed JavaScript - there's a function definition (`handlePromptWithTimeout`) that's inserted in the middle of an object literal where the `onHide` callback should be, breaking the syntax.

### Expected behavior

The prompt dialog should display normally and the application should not crash. The `onHide` callback should be properly defined within the object structure.

### System Info

- Insomnia version: latest
- OS: macOS / Windows / Linux

This is blocking any plugin functionality that relies on prompts. The code structure looks corrupted - it seems like a refactoring was started but not completed properly, leaving invalid JavaScript syntax.

---
Repository: /testbed
