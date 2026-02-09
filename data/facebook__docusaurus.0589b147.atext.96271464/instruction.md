# Bug Report

### Bug: Email autolink parsing broken after recent changes

I'm encountering an issue with email autolink parsing that seems to have been introduced recently. Email addresses in markdown are no longer being recognized correctly.

### Reproduction
When trying to parse markdown with email autolinks, they're not being tokenized properly:

```markdown
Contact me at user@example.com for more info.
```

The email address should be automatically converted to a link, but it's not working anymore. It seems like the @ symbol handling might be broken.

### Expected behavior
Email addresses should be automatically detected and converted to `mailto:` links according to GFM (GitHub Flavored Markdown) spec.

### Additional context
This appears to affect the `tokenizeEmailAutolink` function in the remark-gfm parser. The logic for detecting the @ symbol in email addresses seems to have changed and is causing the parser to fail on valid email addresses.

---
Repository: /testbed
