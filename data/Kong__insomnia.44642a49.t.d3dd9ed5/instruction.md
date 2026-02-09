# Bug Report

### Describe the bug

After a recent update, the application fails to start. There appears to be a syntax error in the `misc.ts` file that's preventing compilation. The error seems to be related to duplicate function definitions or incomplete code in the `keyedDebounce` function.

### Reproduction

1. Pull the latest changes
2. Try to build or run the application
3. Build fails with syntax errors

The issue appears to be in `packages/insomnia/src/common/misc.ts` around the `keyedDebounce` function. There seems to be duplicate/malformed code that's breaking the TypeScript compilation.

### Expected behavior

The application should compile and start successfully without syntax errors.

### System Info
- Package: @insomnia/insomnia
- File affected: `packages/insomnia/src/common/misc.ts`

---
Repository: /testbed
