#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Before the task begins, the following files exist in <code>/home/user/restore_test</code>:
# 
# <pre>
# /home/user/restore_test/file1.bak (contents: "DATA1")
# /home/user/restore_test/file2.bak (contents: "DATA2")
# /home/user/restore_test/file3.bak (contents: "DATA3")
# </pre>
# 
# After correct completion, the following files should exist:
# 
# <code>/home/user/restore_test/Makefile</code> (contents specified below)
# <code>/home/user/restore_test/file1.bak</code> (unchanged, contents: "DATA1")
# <code>/home/user/restore_test/file2.bak</code> (unchanged, contents: "DATA2")
# <code>/home/user/restore_test/file3.bak</code> (unchanged, contents: "DATA3")
# <code>/home/user/restore_test/file1.restored</code> (contents: "DATA1")
# <code>/home/user/restore_test/file2.restored</code> (contents: "DATA2")
# <code>/home/user/restore_test/file3.restored</code> (contents: "DATA3")
# 
# The <code>/home/user/restore_test/Makefile</code> <b>must</b> define a target named <code>restore</code> such that, when <code>make restore</code> is run from <code>/home/user/restore_test</code>, it creates the three <code>.restored</code> files as described above. For each file restored, the command must output exactly one line to <code>stdout</code> in the following format:
# 
# <pre>
# Restored: file1.bak → file1.restored
# Restored: file2.bak → file2.restored
# Restored: file3.bak → file3.restored
# </pre>
# 
# The order of the lines is not important, but the format must match exactly as specified: "Restored: &lt;original&gt; → &lt;restored&gt;", no extra spaces, punctuation, or blank lines.
# 
# Permissions: All files in <code>/home/user/restore_test</code> are owned by <code>user</code>, and are writable and readable by <code>user</code>.
# 
# No files should be deleted or renamed.

echo 'No automated solution provided.'
