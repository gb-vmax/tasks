# Bug Report

### Describe the bug

I'm experiencing an issue with parsing inline directives in markdown. It seems like certain character codes are being checked incorrectly, which causes the parser to fail or behave unexpectedly when processing directive syntax.

### Reproduction

When trying to parse inline directives with specific syntax patterns, the parser doesn't handle them correctly:

```markdown
:directiveName[label text]{attributes}
```

The issue appears to be related to how the parser checks for specific characters (like colons, brackets, and braces) in the directive syntax. The parser seems to be checking for the wrong character codes in certain positions, causing it to reject valid directive syntax or accept invalid syntax.

### Expected behavior

The parser should correctly identify and process inline directives with the proper syntax:
- After the directive name, it should check for the correct delimiter
- When processing labels and attributes, it should look for the appropriate opening/closing characters

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems like it might be a regression or typo in the character code checks. The parser is checking for character code 91 (opening bracket) twice in one case, and checking for 93 (closing bracket) instead of 123 (opening brace) in another case.

---
Repository: /testbed
