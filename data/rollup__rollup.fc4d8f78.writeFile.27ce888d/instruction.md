# Bug Report

### Describe the bug

I'm experiencing issues when loading config files in certain environments. The config file seems to be imported before it's fully written to disk, causing intermittent failures where the config is undefined or partially loaded.

### Reproduction

This happens when:
1. Running rollup with a config file that needs to be bundled
2. The config file gets written to a temporary location
3. The import happens too quickly before the write operation completes

The issue appears to be race condition related - sometimes it works, sometimes it doesn't. It's more frequent on slower file systems or when the config file is larger.

### Expected behavior

The config file should be reliably loaded after being written to disk. The import should only happen after the write operation has completed successfully.

### System Info
- OS: Various (seen on both Linux and Windows)
- Node version: 18.x

This seems like a timing issue where the file import is happening before the file write is finished. Would appreciate any insights on this!

---
Repository: /testbed
