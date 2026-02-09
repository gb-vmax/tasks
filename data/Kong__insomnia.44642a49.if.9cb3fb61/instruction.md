# Bug Report

### Describe the bug

The application crashes on startup with a syntax error in the local-storage module. It appears that some code was accidentally inserted in the wrong location, causing the file to have invalid JavaScript syntax.

### Reproduction

1. Start the application
2. Application fails to load with a parsing error

The error occurs in `packages/insomnia/src/main/local-storage.ts` where there seems to be malformed code structure - class properties and methods are being declared inside a try-catch block instead of at the class level.

### Expected behavior

The application should start normally without any syntax errors. The LocalStorage class should be properly structured with all class properties and methods defined at the appropriate scope level.

### System Info
- Insomnia version: latest
- OS: All platforms affected

This is blocking the application from starting at all, so it's pretty critical. Thanks!

---
Repository: /testbed
