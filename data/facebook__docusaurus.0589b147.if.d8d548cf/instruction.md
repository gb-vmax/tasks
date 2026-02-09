# Bug Report

### Describe the bug

After a recent update, I'm seeing warning messages being logged even when there are no unused directives in my MDX files. The warning appears on every MDX file during build, regardless of whether it actually contains any unused directives.

### Reproduction

1. Create a clean MDX file without any directives
2. Run the build process
3. Observe that a warning message is logged for the file even though there are no unused directives

Example MDX file:
```md
# My Page

This is a simple page with no directives.
```

### Expected behavior

The warning should only be logged when there are actually unused directives present in the file. Clean MDX files without any directives should not trigger warnings.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing a lot of noise in the build output and making it harder to spot actual issues. Would appreciate a fix for this!

---
Repository: /testbed
