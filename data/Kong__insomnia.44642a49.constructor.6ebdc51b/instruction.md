# Bug Report

### Describe the bug

After a recent update, the application fails to start and crashes during initialization. The error occurs when the LocalStorage class is being instantiated, preventing the app from launching completely.

### Reproduction

The crash happens immediately on startup. Looking at the logs, it appears to be related to the LocalStorage initialization code. The application worked fine before the update but now fails to initialize properly.

Steps to reproduce:
1. Launch the application
2. Application crashes during startup
3. Check logs - error occurs during LocalStorage constructor execution

### Expected behavior

The application should start normally and initialize the LocalStorage without crashing. The LocalStorage constructor should complete successfully and allow the app to continue loading.

### System Info
- OS: Various (reproduced on Windows, macOS, Linux)
- Version: Latest main branch

### Additional context

This is a critical issue as it completely blocks the application from starting. The crash appears to be happening in the constructor of the LocalStorage class during the initialization phase.

---
Repository: /testbed
