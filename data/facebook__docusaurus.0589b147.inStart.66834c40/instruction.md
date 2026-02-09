# Bug Report

### Describe the bug

I'm encountering an issue with directive leaf parsing in remark-directive. When using leaf directives (`:directive:`), the parser seems to be exiting with the wrong token type and calling the wrong callback, which causes the directive to fail parsing.

### Reproduction

```markdown
:myDirective:
```

When this is parsed, the directive is not recognized correctly. It appears that the tokenizer is exiting with `"directiveLeafName"` instead of `"directiveLeafSequence"` and passing `nok` instead of `afterName` as the success callback.

### Expected behavior

The directive should be parsed successfully and the correct token sequence should be generated. The tokenizer should:
1. Exit the sequence token correctly
2. Call the proper success callback after parsing the name

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
