# Bug Report

### Describe the bug

After a recent update, autolink detection in markdown is behaving incorrectly. URLs and email addresses are being linked when they shouldn't be, or parts of text that aren't valid URLs/emails are being converted to links.

### Reproduction

The issue appears when processing markdown text with URLs or email-like patterns:

```js
// Example 1: URL detection
const text1 = "Check out example.com for more info"
// This is being incorrectly converted to a link even without a protocol

// Example 2: Email detection  
const text2 = "Contact support@company"
// Partial email addresses (without proper domain) are being linked

// Example 3: Text with dots
const text3 = "The file.name.here should not be a link"
// Random text with dots is being treated as a URL
```

### Expected behavior

- Only valid URLs with proper protocols (http://, https://) or www prefix should be autolinked
- Only complete email addresses with valid domain extensions should be autolinked
- Regular text containing dots or @ symbols should not be automatically converted to links

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

This seems to have started after the latest changes to the autolink literal transformation logic. The regex patterns for URL and email detection appear to be too permissive now.

---
Repository: /testbed
