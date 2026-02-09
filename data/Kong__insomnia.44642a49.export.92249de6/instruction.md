# Bug Report

### Describe the bug
The gRPC send button is showing the wrong state and button text. When a gRPC request is running, it displays the "Send"/"Start" button instead of the "Cancel" button. Also, the button text for unary vs streaming methods appears to be swapped.

### Reproduction
1. Open a gRPC request with a unary method type
2. Click the send button to start the request
3. While the request is running, the button should show "Cancel" but instead shows "Send"
4. For streaming methods, the button shows "Start" when it should show "Send"

### Expected behavior
- When `running` is `true`, the button should display "Cancel" with a stop icon
- When `running` is `false`:
  - For unary methods: button should show "Send"
  - For streaming methods: button should show "Start"

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
