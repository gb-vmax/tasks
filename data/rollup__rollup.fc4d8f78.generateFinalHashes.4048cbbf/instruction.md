# Bug Report

### Describe the bug

I'm experiencing an issue with hash collision handling in the build output. When two chunks happen to generate the same hash, the collision resolution mechanism doesn't work properly and the build gets stuck in an infinite loop.

### Reproduction

This seems to happen when:
1. Multiple chunks are generated with similar content
2. The hash function produces a collision (same hash for different content)
3. The collision resolution tries to rehash but uses the wrong input

I noticed this when building a project with many small chunks that have similar structures. The build process hangs and never completes.

### Expected behavior

When a hash collision occurs, the system should rehash using the previous hash value to generate a new unique hash, allowing the build to complete successfully. Instead, it appears to be rehashing the same value repeatedly, causing an infinite loop.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

Has anyone else encountered this? It's blocking our production builds.

---
Repository: /testbed
