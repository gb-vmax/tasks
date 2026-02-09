# Bug Report

### Describe the bug

I'm encountering an issue when duplicating request groups (folders) in Insomnia. The application crashes or becomes unresponsive when trying to duplicate a folder that has a parent. It seems like something is broken in the duplication logic.

### Reproduction

1. Create a workspace with a folder structure
2. Create a folder inside another folder (nested folder)
3. Try to duplicate the nested folder
4. The application crashes or hangs

I noticed this started happening recently. When I duplicate a top-level folder (one without a parent), it works fine. But as soon as I try to duplicate a folder that's nested inside another folder, the app becomes unresponsive.

### Expected behavior

Duplicating a nested folder should work the same way as duplicating a top-level folder. The duplicated folder should appear with a "(Copy)" suffix in the name, and the application should remain responsive.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
