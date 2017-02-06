param (
    #[string]$scriptPath = 'C:\Charles\Hugo\charlesjlee-website',
    [string]$scriptPath = $PSScriptRoot,
    #[string]$objectsToKeep = ('public','CNAME'),
    [Parameter(Mandatory=$true)][string]$commitMessage
)
$objectsToKeep = ('public','CNAME')
write-output $commitMessage

# commit master
git add .
git commit -m $commitMessage

# commit gh-pages using /public
hugo
git checkout gh-pages
Remove-Item -recurse $scriptPath -exclude $objectsToKeep -force
robocopy public $scriptPath
Remove-Item public -Force -Recurse
git commit -m $commitMessage

# clean-up
git checkout master

# push to GitHub
git push origin master
git push origin gh-pages

# sleep before closing window for a chance to read output
Start-Sleep 5

# setup rsa token
