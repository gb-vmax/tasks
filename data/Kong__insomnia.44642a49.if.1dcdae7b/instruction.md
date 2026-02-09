# Bug Report

### Describe the bug

After a recent update, the application is experiencing startup hangs and extremely slow performance when accessing local storage. The app sometimes freezes for several seconds during initialization, and in some cases, it becomes completely unresponsive.

### Reproduction

The issue occurs during normal application startup:

1. Launch the application
2. The app hangs or becomes very slow during initialization
3. Eventually continues but with noticeable delays

This happens consistently on every startup, making the application nearly unusable. The problem seems to be related to file I/O operations when reading from local storage.

### Expected behavior

The application should start up quickly without any noticeable delays or hangs. Local storage operations should be fast and non-blocking.

### Additional context

- The issue started appearing after the latest update
- CPU usage spikes to 100% during the hang
- Sometimes the app completely freezes and needs to be force-quit
- The problem is more severe on machines with slower disk I/O

This is severely impacting usability. Any help would be appreciated!

---
Repository: /testbed
