
settings.json under .vscode
If not exist, create it by Settings (Gear Icon) > Settings > Workspace > Open Settings (Top Right)



{
    "python.envFile": "${workspaceFolder}/.venv",
    "python.terminal.activateEnvInCurrentTerminal": true

    "git.autofetch": true,
    "git.enableSmartCommit": true,
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "120"
    ],
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length",
        "120"
    ],
    "[python]": {
        "editor.formatOnType": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}



pip install black
pip install flake8
