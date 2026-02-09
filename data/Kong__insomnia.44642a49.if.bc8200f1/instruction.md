# Bug Report

### Describe the bug

There's a syntax error in the environment validation code that prevents the application from starting. It looks like there's duplicate code or malformed function definitions in the `environment-utils.ts` file.

### Reproduction

1. Try to start the application after the latest changes
2. The application fails to load due to a JavaScript syntax error
3. Looking at the environment-utils file, there appear to be duplicate `ensureKeyIsValid` function definitions and orphaned return statements

```typescript
// The file seems to have:
// 1. A function definition
// 2. An export of ensureKeyIsValid
// 3. Then more return statements that aren't part of any function
```

### Expected behavior

The application should start normally and the environment key validation should work correctly.

### System Info
- Insomnia version: latest
- OS: N/A (syntax error prevents startup)

---
Repository: /testbed
