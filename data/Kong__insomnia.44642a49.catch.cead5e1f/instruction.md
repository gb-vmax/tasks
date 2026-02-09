# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use git sync functionality. The application fails to start and throws an error about unexpected token in the git-vcs module.

### Reproduction

1. Start the application with git sync enabled
2. Try to perform any git operation (pull, push, or read from repository)
3. Application crashes with syntax error

The error seems to be related to the `readObjFromTree` method in the GitVCS class. Looking at the code, it appears there might be malformed code structure causing the parser to fail.

### Expected behavior

The git sync operations should work normally without any syntax errors. The application should start up successfully and allow reading objects from the git tree.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking all git sync functionality for me. Any help would be appreciated!

---
Repository: /testbed
