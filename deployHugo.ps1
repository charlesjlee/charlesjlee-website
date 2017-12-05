param (
    [Parameter(Mandatory=$true)][string]$commitMessage
)

# abort if no changes to commit
If (-Not (git status --porcelain)) {
	"No changes to commit. Aborted!"
	exit
}

"Deleting old publication"
Remove-Item .\public -Force -Recurse -ErrorAction Ignore
mkdir public | out-null
git worktree prune
Remove-Item .git\worktrees\public\ -Force -Recurse -ErrorAction Ignore

"Checking out gh-pages branch into public"
git worktree add -B gh-pages public origin/gh-pages

"Removing existing files"
Remove-Item .\public\* -Force -Recurse

"Generating site"
hugo --quiet
'charlesjlee.com' | Out-File -filepath '.\public\CNAME' -NoNewline

"Committing master branch"
git add --all
git commit -m $commitMessage

"Committing gh-pages branch"
Push-Location -path public
git add --all
git commit -m $commitMessage

"Pushing master to Github"
git push origin master

"Pushing gh-pages branch to Github"
git push origin gh-pages

# pop back to Hugo folder
Pop-Location

# sleep before closing window for a chance to read output
#Start-Sleep 5

# setup rsa token
