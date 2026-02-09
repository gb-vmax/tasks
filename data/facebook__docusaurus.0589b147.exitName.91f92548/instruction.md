# Bug Report

### Describe the bug

I'm experiencing an issue with directive name parsing in nested directive structures. When using text directives inside container or leaf directives, the name assignment seems to be going to the wrong node level.

### Reproduction

```markdown
::container-directive
:text-directive[content]
::
```

When parsing the above structure, the text directive's name appears to be incorrectly assigned or causing unexpected behavior. The parser seems to be looking at the wrong stack position when trying to set the directive name.

### Expected behavior

Each directive type (container, leaf, and text) should have its name properly assigned to the correct node in the AST, regardless of nesting level. Text directives nested within container or leaf directives should maintain their own names without interfering with parent directive names.

### System Info
- remark-directive version: 3.0.0
- Node version: latest

This seems to have started happening recently and is affecting markdown parsing with nested directives. Any help would be appreciated!

---
Repository: /testbed
