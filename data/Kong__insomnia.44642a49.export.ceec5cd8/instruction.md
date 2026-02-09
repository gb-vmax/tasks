# Bug Report

### Describe the bug

The gRPC send button is showing the wrong state - it displays "Cancel" when the request is not running and shows the "Start" button when a request is actually in progress. The button states appear to be completely inverted from what they should be.

### Reproduction

1. Open a gRPC request
2. Click the send button to start a request
3. Observe that the button still shows as if it's ready to start instead of showing "Cancel"
4. When no request is running, the button incorrectly shows "Cancel"

### Expected behavior

- When `running` is `true`, the button should display "Cancel" and allow stopping the request
- When `running` is `false`, the button should display the appropriate start action based on the method type
- The button states should correctly reflect the actual running state of the gRPC request

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
