# Bug Report

### Describe the bug

The app context is broken after a recent change. When trying to use the prompt functionality, I'm getting syntax errors and the application fails to load. It looks like there's a malformed code structure in the app context file.

### Reproduction

1. Try to use any plugin that calls `app.prompt()`
2. The application throws a syntax error
3. Looking at the code, there appears to be duplicate/nested function definitions that don't make sense

The code structure looks wrong - there's a `prompt()` function definition that appears in the middle of another object/function definition, and there are duplicate `onHide()` callbacks. This is causing the entire plugin system to fail.

### Expected behavior

The `app.prompt()` method should work correctly and display a prompt dialog. The code should be properly structured without syntax errors.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking me from using any plugins that need to prompt the user for input. Please fix the code structure in `packages/insomnia/src/plugins/context/app.tsx`.

---
Repository: /testbed
