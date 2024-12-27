import subprocess

print()
print('Compiling Hugo...')
subprocess.run(f'hugo')

print()
commit_msg = str(input('Commit message : '))

print()
print('Commiting to Github...')
subprocess.run(f'git add .')
subprocess.run(f'git commit -m "{commit_msg}"')
subprocess.run('git push origin main')
print('Done pushing to master branch!')

push_to_branch = str(input('Push to public branch? (y/n) '))

if push_to_branch == 'y':
    print()
    print('Pushing to public branch...')
    subprocess.run('git subtree split --prefix public -b pub-branch')
    subprocess.run('git push origin pub-branch:public --force')
    subprocess.run('git branch -D pub-branch')
    print('Done! All step has been successfully run.')

else:
    print('Done! Successfully push to master branch and not pushing to public branch.')