Hey, I need some help with a mobile build pipeline config. We have an INI-format build configuration file at `/home/user/pipeline/build.ini` that controls our Android and iOS CI builds. I need you to extract specific values from it and write them to a summary file so our deployment script can quickly read the essential build parameters without parsing the full INI file.

Here's what I need:

Parse `/home/user/pipeline/build.ini` and create a new file at `/home/user/pipeline/build_summary.txt` that contains exactly the following key-value pairs, one per line, in this exact order:

1. The value of `app_name` from the `[project]` section
2. The value of `version_name` from the `[project]` section
3. The value of `version_code` from the `[project]` section
4. The value of `build_type` from the `[android]` section
5. The value of `min_sdk` from the `[android]` section
6. The value of `target_sdk` from the `[android]` section
7. The value of `scheme` from the `[ios]` section
8. The value of `deployment_target` from the `[ios]` section

Each line in `build_summary.txt` must follow this exact format:
```
KEY=VALUE
```

Use the key names exactly as listed above (lowercase, with underscores), and the values exactly as they appear in the INI file (no surrounding whitespace). There should be no blank lines in the output file, no section headers, no comments — just those 8 lines in the order listed.

For example, if `app_name` is `MyApp`, the first line should be:
```
app_name=MyApp
```

The file should have a trailing newline (i.e., the last line ends with a newline character, as is standard for text files on Linux).

Can you parse the INI file and generate the summary?
