# Bug Report

### Bug: Translation warnings showing incorrect file path information

I noticed something weird with the translation extraction warnings. When I have multiple files with translation warnings, the warning messages are showing the wrong warnings for each file.

### Reproduction

Let's say I have two files with translation issues:
- `file1.tsx` has warning: "Missing translation key 'header.title'"
- `file2.tsx` has warning: "Invalid translation format for 'footer.text'"

When the extraction runs, both files show the same warning message (the one from the first file), instead of showing their respective warnings.

### Expected behavior

Each file should display its own specific warnings, not the warnings from the first file in the list.

### Additional context

This makes it really hard to debug translation issues since you can't tell which file actually has which problem. The file paths in the log messages are correct, but the warning content itself is always from the first file.

---
Repository: /testbed
