# Bug Report

### Describe the bug

I'm experiencing an issue with git operations on Windows where file paths are not being handled correctly. When checking the status of files, the operation fails because the filepath parameter is not being converted to POSIX format before being passed to the git library.

### Reproduction

On Windows:
1. Initialize a git repository in a project
2. Try to check the status of a file with a Windows path (e.g., `folder\subfolder\file.json`)
3. The git status operation fails or returns incorrect results

The issue appears to be in the `status` method where the filepath conversion is being applied to the wrong object.

### Expected behavior

File paths should be properly converted from Windows format (backslashes) to POSIX format (forward slashes) before being passed to the git library, similar to how it's done in other methods like `add()`.

### System Info
- OS: Windows 10/11
- Version: Latest

---
Repository: /testbed
