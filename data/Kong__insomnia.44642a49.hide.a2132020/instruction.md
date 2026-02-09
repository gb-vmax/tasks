# Bug Report

### Describe the bug

I'm experiencing an issue with the template tag encoding field visibility logic. The encoding dropdown for base64 is not showing up correctly when it should be visible based on the selected filter type.

### Reproduction

When using template tags with certain filter types, the base64 encoding option appears when it shouldn't, or doesn't appear when it should. The visibility logic seems to be inverted or not handling all the expected filter types properly.

Steps to reproduce:
1. Create a template tag with a filter argument
2. Select a filter type like 'raw' or 'url'
3. Notice the encoding field visibility doesn't match expected behavior
4. Try with 'request-url' filter - the encoding field behavior is inconsistent

### Expected behavior

The base64 encoding field should be hidden for filter types: 'raw', 'url', and 'request-url'. For other filter types (like 'body', 'header', etc.), the encoding field should be visible and available for selection.

Currently the logic appears to be backwards - it's hiding when it should show and showing when it should hide for certain filter combinations.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
