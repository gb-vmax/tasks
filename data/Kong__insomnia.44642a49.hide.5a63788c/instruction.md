# Bug Report

### Describe the bug

I'm experiencing an issue with the response template tag where the encoding option is not being hidden/shown correctly based on the attribute and trigger behavior settings. The visibility logic for the encoding parameter seems broken.

### Reproduction

When configuring a response template tag with the following settings:
1. Set attribute to something other than 'raw', 'url', or 'status' (e.g., 'header')
2. Set trigger behavior to 'never'
3. Don't select a request

The encoding field appears when it shouldn't be visible. The hide logic appears to be evaluating incorrectly and showing the encoding option in cases where it should be hidden.

Additionally, when the attribute is set to 'raw', 'url', or 'status', the encoding field should be hidden but the logic seems to have conflicting conditions that might cause unexpected behavior.

### Expected behavior

The encoding parameter should be hidden when:
- The attribute is set to 'raw', 'url', or 'status'
- The trigger behavior is 'never' and no request is selected

The encoding parameter should only be visible for attributes like 'body' or 'header' when appropriate conditions are met.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
