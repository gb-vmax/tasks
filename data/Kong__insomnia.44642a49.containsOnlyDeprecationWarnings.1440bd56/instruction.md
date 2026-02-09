# Bug Report

### Describe the bug

After installing a plugin, I'm seeing duplicate deprecation warnings being logged multiple times in the console. Each warning appears to be printed separately even when it's the same underlying issue, making it difficult to understand what's actually deprecated.

### Reproduction

When installing a plugin that has deprecated dependencies (e.g., using `npm` or `yarn`), the console output shows the same deprecation warning repeated multiple times instead of being grouped together. 

For example, if a plugin depends on multiple packages that all use the same deprecated dependency, each occurrence gets logged individually rather than being consolidated.

### Expected behavior

Deprecation warnings should be deduplicated and grouped together with a count indicator (e.g., "warning message (×3)") to make the output cleaner and easier to understand. It would also be helpful to have a summary showing the total number of unique warnings by severity level.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
