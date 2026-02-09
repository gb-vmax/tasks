# Bug Report

### Describe the bug

The application fails to start after a recent update. There appears to be a syntax error in the `wrapper-modal.tsx` file that's preventing compilation.

### Reproduction

1. Pull the latest changes
2. Try to start the application
3. Build/compilation fails with syntax errors

### Expected behavior

The application should compile and start successfully without any syntax errors.

### Additional context

Looking at the code, it seems like there's duplicate/malformed code in the `WrapperModal` component. The `useImperativeHandle` hook appears to be defined multiple times or has incorrect structure, which is causing the compilation to fail.

---
Repository: /testbed
