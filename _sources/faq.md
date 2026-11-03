# 🙋 FAQ

## Git: checkout, reset, clean, and revert

Let's delve into the details of each of these Git commands: `checkout`, `reset`, `clean`, and `revert`. Each serves a unique purpose in managing your Git repository.

### 1. `git checkout`
The `git checkout` command is used for switching branches or restoring working tree files. It can be employed in several contexts, and it's quite powerful in its flexibility.

#### Key Uses:
- **Switching Branches**: You can switch between different branches in your repository.
  ```bash
  git checkout branch_name
  ```
- **Restoring Files**: You can restore specific files to their state at a particular commit, or discard changes in the working directory.
  ```bash
  git checkout -- path/to/file
  ```

The command `git checkout -- .` is used in Git to discard any uncommitted changes in the working directory. Here's a breakdown of what it does:

- `git checkout`: This command is used to switch branches or restore working tree files.

- `--`: This option indicates that what follows are paths, and not branch names. It helps Git to distinguish between branch names and file paths.

- `.`: The dot represents the current directory and all its contents.

When combined, git checkout -- . tells Git to discard any changes to tracked files in the current directory and its subdirectories. Any modifications, deletions, or additions that haven't been committed will be reverted to their last committed state.

### 2. `git reset`
The `git reset` command is used to undo changes. It has various options that can adjust the scope of what you undo, ranging from just the index to also modifying the working directory.

#### Key Uses:
- **Soft Reset**: Resets the HEAD to a previous commit but keeps the changes in the index and working directory. This allows you to re-commit the changes.
  ```bash
  git reset --soft HEAD~1
  ```
- **Mixed Reset (default)**: Resets the HEAD and index to a previous commit but keeps the changes in the working directory.
  ```bash
  git reset HEAD~1
  ```
- **Hard Reset**: Resets the HEAD, index, and working directory to a previous commit. This will discard all changes.
  ```bash
  git reset --hard HEAD~1
  ```

### 3. `git clean`
The `git clean` command is used to remove untracked files and directories from the working directory. This is helpful for cleaning up your working directory by getting rid of files that aren't under version control.

#### Key Uses:
- **Remove Untracked Files**:
  ```bash
  git clean -f
  ```
- **Remove Untracked Directories**:
  ```bash
  git clean -d
  ```
- **Interactive Mode**: Prompts before each removal.
  ```bash
  git clean -i
  ```

### 4. `git revert`
The `git revert` command is used to create a new commit that undoes the changes made by a previous commit. This is different from `git reset` in that `git revert` maintains the history of the commit being undone.

#### Key Uses:
- **Reverting a Commit**: Creates a new commit that undoes the changes of a specified commit.
  ```bash
  git revert commit_hash
  ```

### Summary:
- **`checkout`**: Switches branches or discards changes in the working directory.
- **`reset`**: Resets the state of HEAD, index, and working directory to a previous commit.
- **`clean`**: Removes untracked files and directories.
- **`revert`**: Creates a new commit that undoes the changes of a previous commit, preserving the history.

Each of these commands offers powerful ways to manage your Git repository and ensures that you can control and revert changes as needed. 

## Git: How to discard local changes

To discard your local changes and make your branch match the remote branch, you can follow these steps. Make sure you’re ready to lose any changes you’ve made locally, as this will revert your working directory to match the state of the remote repository.

1. **Reset the Branch**: This will reset your branch to match the remote branch. Any changes in your working directory will be kept, but they will be untracked.

   ```bash
   git reset --hard origin/main
   ```

   - **`--hard`**: This option discards all local changes.

2. **Clean Untracked Files**: This will remove any untracked files or directories.

   ```bash
   git clean -fd
   ```

   - **`-f`**: This option forces the removal.
   - **`-d`**: This option removes untracked directories in addition to untracked files.

After running these commands, your local branch should match the remote branch, and any local changes will be discarded.

Let me know if you need help with anything else! 😊