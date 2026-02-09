# Bug Report

### Describe the bug

I'm encountering a syntax error in the `properties.ts` file after a recent update. The code appears to have malformed structure where a method definition is inserted in the middle of an if-else block, causing the file to not compile properly.

### Reproduction

When trying to use any functionality from the properties module, the application fails to build with a syntax error. The issue seems to be in the `PropertyBase` class where the code structure is broken.

Looking at the `findInParents` method, it appears that method definition code has been inserted inside an existing conditional block instead of being properly placed as a separate method.

### Expected behavior

The code should compile without syntax errors and the `findInParents` method should be properly defined as a class method, not embedded within another conditional statement.

### System Info
- Package: insomnia-sdk
- File: packages/insomnia-sdk/src/objects/properties.ts

This is blocking our ability to build the project. Any help would be appreciated!

---
Repository: /testbed
