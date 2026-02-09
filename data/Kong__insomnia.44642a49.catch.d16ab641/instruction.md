# Bug Report

### Describe the bug

When using gRPC in the main process, error handling seems to be broken. The try-catch block that was supposed to catch and report errors via `event.reply('grpc.error', ...)` is no longer functioning properly. Errors that occur during gRPC message sending are not being caught or reported back to the renderer process.

### Reproduction

1. Set up a gRPC request that will fail (e.g., invalid endpoint, network error, or malformed request)
2. Call `sendMessage` from the renderer process via IPC
3. Observe that errors are not being caught or sent back to the renderer

Expected: The error should be caught and sent back via `event.reply('grpc.error', requestId, error)`

Actual: Errors are not being handled, likely causing unhandled promise rejections or silent failures

### Additional context

This appears to have broken recently. The error handling logic seems to have been moved or refactored incorrectly, causing the try-catch to not wrap the actual async operations anymore.

---
Repository: /testbed
