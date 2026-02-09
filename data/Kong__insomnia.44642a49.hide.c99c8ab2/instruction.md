# Bug Report

### Describe the bug
There's a syntax error in the ErrorModal component that prevents the application from compiling. The code has an interface definition appearing in the middle of the `useImperativeHandle` hook implementation, which breaks the JavaScript/TypeScript syntax.

### Reproduction
1. Try to build or run the application
2. The build fails with a syntax error in `error-modal.tsx`

The issue is in the `useImperativeHandle` hook where an interface definition (`ErrorModalOptions`) is incorrectly placed inside the object literal being returned, right before the `hide` method.

### Expected behavior
The application should compile and run without syntax errors. The ErrorModal component should work correctly with proper TypeScript type definitions.

### System Info
- Insomnia version: latest
- Node version: (any)

This looks like it might have been introduced during a refactoring or merge conflict resolution. The interface definition needs to be moved outside of the `useImperativeHandle` implementation.

---
Repository: /testbed
