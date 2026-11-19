$ProjectRoot = "$PSScriptRoot\..\.."

# if there is a poetry env to invoke
# # poetry config virtualenvs.in-project false --local
$poetry_env_list=$(poetry env list)
& "$env:LOCALAPPDATA/pypoetry/Cache/virtualenvs/$poetry_env_list/Scripts/Activate.ps1"
# poetry config virtualenvs.in-project true --local
# & "$PSScriptRoot\..\..\.venv\scripts\activate.ps1"
$open_me = @(
    "..\..\TODO.md"
)

$open_me | ForEach-Object {
    Write-Host -ForegroundColor Green "code '$_'..."
    code "$PSScriptRoot\$_"
}
