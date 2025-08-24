# 🔨 Software Setup

## 📜 Agenda
- Create a GitHub repository.
- Configure git repository.
- Install and Configure VS Code

```{note}
Don’t worry if it doesn’t work right. If everything did, you’d be out of a job.
```

## 💻 Procedure

(CreateRepo)=
### Create a Repository within the GitHub Classroom

1. If you don't already have a <a href="https://github.com/" target="_blank">GitHub</a> account, go ahead and create one.
1. Once you have your account, browse to <a href="https://classroom.github.com/a/UkcATx9Y" target="_blank">ECE487 Classroom</a>.
1. Select `Accept this assignment`.
1. Browse to your repository. Note the URL for your repository (save this link; it is the best way to check if your repo is updated).
1. Go to `Settings` and change your repository name to `ece487-YourLastName`, e.g., `ece487-baek`.

```{important}
Please name your repository as ece487-LastName. This will help instructors find your repository easily.
```

### Install Git

1. To download `Git for Windows`  go to <a href="https://git-scm.com/download/win" target="_blank">git-scm</a> and click on the link.
1. Run the setup file and install Git with the default settings. If you have a Mac, you don’t need to do this step because Git is already installed on your computer.

### Enable SSH Connection to Your GitHub Account

Skip this section and go [here](CloneRepo) if you already have set up the SSH connection to your GitHub account. 

1. Open `Git Bash` and generate a new SSH key, replacing `"your_email@example.com"` with your actual GitHub email address:

    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```

1. When prompted to “Enter a file in which to save the key,” hit `Enter`.
1. At the prompt for a secure passphrase, press `Enter` to skip it.
1. Start the ssh-agent in the background and add your SSH private key to the ssh-agent:
    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```
1. Display the contents of your public key:
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```

1. Select the output (ensure it include your GitHub email at the end), right click, and select `Copy`.
1. Open a web browser and sign in to your GitHub account.
1. In the upper-right corner, click your profile photo, then click `Settings`.

    ```{image} ./figures/ssh1.png
    :width: 140
    :align: center
    ```
    <br>

1. In the user settings sidebar, click `SSH` and `GPG keys`.

    ```{image} ./figures/settings-sidebar-ssh-keys.png
    :width: 180
    :align: center
    ```
    <br>
1. Click `New SSH key`

    ```{image} ./figures/ssh-add-ssh-key.png
    :width: 480
    :align: center
    ```
    <br>

1. In the `Title` field, add a descriptive label for the new key, such as `HP830 G7`.
1. Paste your SSH key into the `Key` field (contents of the `.pub` file).
1. Click `Add SSH key`.
1. If prompted, confirm your GitHub password.

(CloneRepo)=
### Clone repository to your computer

1. Create a new folder named `ece487_wksp` in your home directory, e.g., `C:\Users\stanley.baek\ece487_wksp`.
1. Right-click on the `ece487_wksp` folder and select `Git Bash Here` from the menu.   
1. From the GitHub repository you created in this [section](CreateRepo), click Clone and copy the command that begins with `git clone` by clicking on the `copy` button as shown below.
    ```{image} ./figures/GitClone.png
    :width: 320
    :align: center
    ```
    <br>
1. Paste it within the Bash terminal (middle-click, right-click > Paste, or Shift+Ins to paste) and add a space followed by a period as shown below. The period at the end means that the destination is the current folder. Hit Enter.
1. If it asks for a password, enter the app password you saved in the previous step.

    **Note**: The gif animation below has been adapted from ECE382. You must use ECE487 in place of ECE382.

    ```{image} ./figures/GitClone.gif
    :width: 680
    :align: center
    ```
    <br>
1. The figure below shows an example of a local `ece487_wksp` folder on your computer.

    ```{image} ./figures/workspace_folder.png
    :width: 740
    :align: center
    ```
    <br>

1. Return to the Git Bash terminal. If it's closed, right-click an empty area inside the `ece487_wksp` folder and select `Git Bash Here` from the menu.
1. Type `git remote -v` and press Enter.  You should see two lines indicating `origin` is your remote repository on GitHub for both fetching and pushing. 
1. Add the instructor's repository as another remote source:

    ```bash
    git remote add upstream https://github.com/ECE487/ece487_ws_2025.git
    ```
1. Verify the upstream repository has been added by typing `git remote -v` and press Enter.  You should now see two additional lines indicating `upstream` is the original repository you forked from.

    ```{image} ./figures/GitAddUpstream.gif
    :width: 640
    :align: center
    ```
    <br>

1. If the instructor updates the code, you will be notified, and you will need to run `git pull upstream main` to get the latest updates.
1. When you push or pull your code, `origin` will be used by default, which points to your own GitHub repository.

    ```{image} ./figures/FetchUpstream.png
    :width: 320
    :align: center
    ```
    <br>

    <center>
    Image is sourced from <a href="https://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github/9257901#9257901" target="_blank">Stack Overflow</a>
    </center>


### Install and Configure VS Code

1. Download <a href="https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe">Python 3.12.10</a>. Run the file and follow the installation steps. Make sure to check the box that says `Add Python to PATH!`
1. Download and install <a href="https://code.visualstudio.com/download" target="_blank">VS Code</a>. Choose the appropriate version for your operating system. 
1. During installation, ensure that you check the last four boxes (see image below) to integrate VS Code with Python and Git.

    ```{image} ./figures/VSCode_Setup.png
    :width: 580
    :align: center
    ```
    <br>

1. To open the `ece487_wksp` folder with VS Code, right-click on the folder and choose `Open with Code` from the menu.
1. Open the `Show All Commands` menu by going to Help or pressing `Shift+Ctrl+P`. This is a frequently used menu - remember the shortcut `Shift+Ctrl+P`.
1. Create a virtual environment for Python typing in the first few letters of `Python: Create Environment` in the `Show All Commands` menu and select it.
1. Choose `Venv` to create a virtual environment.  
1. Select the Python path that you want to use.  
1. Choose `requirements.txt` (`requirements_linux.txt` for Mac or Linux users) to install the Python packages for this course.
1. Wait for a few minutes until all the packages are installed.
1. Click the gear icon at the bottom-left corner and select `Settings`. 
1. Select the `workspace` tab and click the page icon at the top-right corner. This will open `settings.json` 
1. Open `vscode.md`, copy the code inside the curly braces, paste it into `settings.json`, and save the file.
This ensures the virtual environment starts automatically when you open the workspace.

    ```{image} ./figures/VirtualEnvSetup.gif
    :width: 720
    :align: center
    ```
    <br>

### Commit and Push Your Update
1. Open `README.md` and enter your name as the author.  Save the file by pressing `Ctrl+s`.
1. You should see a number 1 next to the `Source Control` icon.  Click on the icon and type **initial commit** in the message box, and then click the arrow next to the `Commit` button. Select `Commit & Push` from the dropdown menu.  

    ```{image} ./figures/GitCommitPush.gif
    :width: 720
    :align: center
    ```
    <br>

1. You can accomplish the same steps in `Git Bash`. 
    - Open `Git Bash` and type
        ```bash
        git add -A
        git commit -m "Initial commit."
        git push
        ```
    - Press `Enter` after each command.
    - If prompted, enter your GitHub username and password.

```{tip}
There are also many third-party graphical user interface (GUI) clients for Git. Explore options at <a href="https://git-scm.com/downloads/guis" target="_blank">Git-SCM GUIs</a>.
```

```{Attention} 
It is your responsibility to verify that your files have been successfully pushed to your GitHub repository. Always visit your GitHub repository after pushing your assignments to ensure everything is correctly uploaded.
```

## 🚚 Deliverables

Take screenshots of the following and submit them via Gradescope.  Use `Snip & Sketch` (Win+Shift+S) on Windows 10 or `Shift+CMD+4` in Mac to capture the screenshots. Save them in `png` or `jpg` format.  

```{warning}
Do **not** take pictures of your computer screen using a mobile device or camera. Doing so will indicate a lack of understanding of sampling aliasing (covered in ECE215, ECE382 & ECE333), and you will lose 30 points. Yes, I’m serious about this.
```

### Deliverable 1
- Push your updates to GitHub

### Deliverable 2
- Provide a screenshot of your VS Code as shown below. Ensure that the `.venv` and `.vscode` folders are visible under the `EXPLORER` window.
```{image} ./figures/VSCode_Configured.png
:width: 620
:align: center
```
<br>
