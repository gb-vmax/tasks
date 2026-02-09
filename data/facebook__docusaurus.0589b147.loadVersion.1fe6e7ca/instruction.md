# Bug Report

### Describe the bug

After a recent update, I'm seeing error messages in the console even when documentation versions are loading successfully. The error log says "Loading of version failed for version name=..." but the build completes without any actual failures.

### Reproduction

1. Set up a Docusaurus project with versioned docs
2. Run the build process
3. Observe console output

Expected: No error messages when versions load successfully
Actual: Error messages appear even though everything works fine

### Additional context

The error message appears for every version being loaded, which is confusing because the build doesn't actually fail. It seems like the logging is happening at the wrong time or in the wrong place.

System:
- Docusaurus: latest
- Node: v18.x

---
Repository: /testbed
