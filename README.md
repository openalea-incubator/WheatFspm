# WheatFspm

WheatFspm contains a set of sub-packages (named in git submodules):
* CN-Wheat: 
* Elong Wheat: 
* ...

## Developers

This  package contains [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) ([in French](https://git-scm.com/book/fr/v2/Utilitaires-Git-Sous-modules)).

Development is done in the different submodules.

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

