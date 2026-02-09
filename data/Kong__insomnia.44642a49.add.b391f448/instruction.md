# Bug Report

### Describe the bug

I'm experiencing an issue with the git integration where adding files to staging seems to hang or take an extremely long time when dealing with renamed files. The application becomes unresponsive during git operations that previously worked fine.

### Reproduction

1. Create a file in your workspace (e.g., `test.json`)
2. Commit the file
3. Rename the file to something else (e.g., `test-renamed.json`)
4. Try to stage the changes using the git sync feature
5. The operation takes forever or the app becomes unresponsive

### Expected behavior

Staging renamed files should be quick and not cause the application to hang. Previously, adding files to the git index was nearly instantaneous regardless of whether files were renamed or not.

### Additional context

This seems to have started happening recently. I have a workspace with about 50-60 files, and when I rename a few files and try to stage them, the whole sync process just freezes up. Sometimes I have to force quit the app.

The issue is particularly noticeable when:
- Multiple files are renamed at once
- The workspace has a larger number of files
- Using wildcard patterns (though I'm not sure if that's related)

---
Repository: /testbed
