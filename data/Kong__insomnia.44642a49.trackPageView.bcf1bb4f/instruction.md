# Bug Report

### Describe the bug

After a recent update, the application fails to start due to a syntax error in the test setup file. The error appears to be related to malformed JavaScript/TypeScript code in the global mock configuration.

### Reproduction

1. Try to run the application or any tests
2. The setup file fails to parse
3. Application/tests cannot start

The issue seems to be in `packages/insomnia/src/__jest__/setup.ts` where the `global.main` object definition has invalid syntax. There are function definitions appearing outside of the object literal structure, which causes a parsing error.

### Expected behavior

The setup file should have valid JavaScript/TypeScript syntax and the application should start normally. The `global.main` object should be properly structured with all properties and methods defined correctly within the object literal.

### System Info
- Node version: Latest
- Package: @insomnia/insomnia

This is blocking all development work as nothing can run with this syntax error present. Would appreciate a quick fix!

---
Repository: /testbed
