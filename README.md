# WheatFspm

WheatFspm contains a set of sub-packages (named in git submodules):
* CN-Wheat: 
* Elong Wheat: 
* ...

## Developers

### Cloning

To clone the project, please use:

    git clone --recurse-submodules https://github.com/openalea-incubator/WheatFspm

### Updating submodules

If you want to update all submodules:

    git submodule update --remote

Otherelse , o update each one to a specific version, branch or tag, do:

    cd mypackage
    git fetch
    git merge origin/master

