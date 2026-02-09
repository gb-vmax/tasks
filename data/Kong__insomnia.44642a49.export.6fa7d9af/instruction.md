# Bug Report

### Describe the bug

The gRPC send button is showing incorrect text and appearing in the wrong state. When no method type is selected, the button is showing "Send"/"Start" text instead of being disabled with "Select Method" text. Additionally, the button labels for unary vs streaming methods seem to be swapped - unary methods show "Start" when they should show "Send", and streaming methods show "Send" when they should show "Start".

### Reproduction

1. Open a gRPC request
2. Don't select a method type yet
3. Notice the send button shows "Send" or "Start" instead of being disabled with "Select Method"
4. Select a unary method
5. The button shows "Start" instead of "Send"
6. Select a streaming method (client/server/bidirectional)
7. The button shows "Send" instead of "Start"

### Expected behavior

- When no method type is selected: Button should be disabled and display "Select Method"
- When a unary method is selected: Button should display "Send"
- When a streaming method is selected: Button should display "Start"

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
