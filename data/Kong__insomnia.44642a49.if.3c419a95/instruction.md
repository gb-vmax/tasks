# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where the application becomes unresponsive when trying to read from local storage. It seems like the app hangs for a brief period before continuing, and this is happening consistently on startup and when accessing certain settings.

### Reproduction

The issue occurs when:
1. Starting the application
2. Accessing any feature that reads from local storage
3. The app freezes/hangs for a second or two before continuing

I noticed this behavior particularly when:
- Opening preferences
- Loading workspace data
- Accessing recently used items

The delay is very noticeable and makes the app feel sluggish. This wasn't happening in previous versions.

### Expected behavior

Local storage reads should be instantaneous without any noticeable delays or hanging. The application should remain responsive at all times.

### System Info
- OS: Windows 10
- Version: Latest main branch

---
Repository: /testbed
