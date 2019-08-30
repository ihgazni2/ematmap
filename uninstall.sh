pip3 uninstall ematmap
git rm -r dist
git rm -r build
git rm -r ematmap.egg-info
rm -r dist
rm -r build
rm -r ematmap.egg-info
git add .
git commit -m "remove old build"

