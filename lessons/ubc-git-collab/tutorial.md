

#To-do:
- exercises
- git hub 
- git rebase
- git fetch+merge vs. pull

## Git- Collaborating

Version control really comes into its own
when we begin to collaborate with other people.
We already have most of the machinery we need to do this:
repositories,
branches,
and the `commit` and `merge` commands.
The last trick is to merge from branches that are in other repositories,
not our own.

Systems like Git and Mercurial allow us to merge changes
between any two repositories.
In practice,
though,
it's easiest to use a definitive master copy as a central hub,
and for that master copy to be on the web rather than on someone's laptop
(so that it's accessible even when that "someone" is off the network).
Most programmers use hosting services like [GitHub](http://github.com) or [BitBucket](http://bitbucket.org)
to hold those master copies;
we'll explore the pros and cons of this in the final section of this lesson,
but will use GitHub until then.

Let's start by sharing the changes we've made to our current project with the world.
Log in to GitHub,
then create a new repository called `planets`
using their GUI:

FIXME: screenshot

This effectively does the following on GitHub's servers:

```
$ mkdir planets
$ cd planets
$ git init
```

We're now in the situation shown in the figure below:

FIXME: diagram

Our local repository still has two branches called `master` and `moons`,
with the same contents as before.
The remote repository on GitHub only has a single branch,
`master`,
and doesn't contain any files yet.

The next step---the crucial one---is to connect the two repositories.
We do this by making the GitHub repository a [remote](glossary.html#remote_repository)
for the local repository.
The home page of the repository on GitHub includes
the string we need to identify it:

FIXME: screenshot

For now,
we'll use the 'http' identifier,
since it requires the least setup.
Copy that string from the browser,
go into the local `planets` repository,
and run this command:

```
$ git remote add origin https://github.com/yourname/planets
```

(using your GitHub ID instead of `yourname`).
We can check that the command has worked by running `git remote -v`:

```
$ git remote -v
origin   https://github.com/yourname/planets.git (push)
origin   https://github.com/yourname/planets.git (fetch)
```

There's nothing special about the name `origin`:
we can use almost anything,
but we'll see in a moment why `origin` is a sensible choice.
Once this is set up,
the following command will push the changes from our local repository's `master` branch
to the corresponding branch in the repository on GitHub:

```
$ git push origin master
Counting objects: 27, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (23/23), done.
Writing objects: 100% (27/27), 2.62 KiB, done.
Total 27 (delta 5), reused 0 (delta 0)
To https://github.com/gvwilson/planets.git
 * [new branch]      master -> master
```

This command just did what `git merge` does,
except it moved changes between repositories
rather than just between branches.
Our local and remote repositories are now in this state:

FIXME: diagram

We can pull changes from the remote repository to the local one as well:

```
$ git pull origin master
From https://github.com/gvwilson/planets
 * branch            master     -> FETCH_HEAD
Already up-to-date.
```

Pulling has no effect in this case
because the two repositories are already synchronized.
If someone else had pushed some changes,
though,
this command would download them to our local repository:

FIXME: diagram

The model shown above,
in which everyone pushes and pulls from a single repository,
is perfectly usable,
but there's one thing it *doesn't* let us do,
and that's [code review](glossary.html#code_review).
Suppose Dracula wants to be able to look at Wolfman's changes
before merging them into the master copy on GitHub,
just as he would review Wolfman's paper before publishing it
(or perhaps even before submitting it for publication).
We need to arrange things so that Wolfman can commit his changes
and Dracula can compare them with the master copy;
in fact,
we want Wolfman to be able to commit many times,
so that he can incorporate Dracula's feedback
and get further review
as often as necessary.

Rather than the model shown above,
most programmers therefore use a slightly more complex model.
When the project starts,
Dracula creates a repository on GitHub
in exactly the same way as we created the `planets` repository a few moments ago,
and then [clones](glossary.html#repository_clone) it to his desktop:

```
$ git clone https://github.com/vlad/undersea.git
Cloning into 'undersea'...
warning: You appear to have cloned an empty repository.
```

`git clone` automatically adds the original repository on GitHub
as a remote of the local repository called `origin`---this
is why we chose `origin` as a remote name in our previous example:

```
$ cd undersea
$ git remote -v
origin	    https://github.com/vlad/undersea.git (fetch)
origin	    https://github.com/vlad/undersea.git (push)
```

Dracula can now push and pull changes just as before.

Wolfman doesn't clone Dracula's GitHub repository directly.
Instead,
he [forks](glossary.html#fork_repository) it,
i.e.,
clones it on GitHub.
He does this using the GitHub web interface:

FIXME: screenshot

He then clones his GitHub repository,
not Dracula's,
to give himself a desktop copy:

FIXME: diagram

This may seem like unnecessary work,
but it allows Wolfman and Dracula to collaborate much more effectively.
Suppose Wolfman makes a change to the project.
He commits it to his local repository,
then uses `git push` to copy those changes to GitHub:

FIXME: diagram

He then creates a [pull request](glossary.html#pull_request),
which notifies Dracula that Wolfman wants to merge some changes
into Dracula's repository:

FIXME: screenshot

A pull request is a merge waiting to happen.
When Dracula views it online,
he can see and comment on the changes Wolfman wants to make:

FIXME: screenshot

Commenting is the crucial step here,
and half the reason Wolfman went to the trouble of forking the repository on GitHub.
Dracula,
or anyone else involved in the project,
can now give Wolfman feedback on what he is trying to do:
this function is too long,
that one contains a bug,
there's a special case that isn't being handled anywhere,
and so on.
Wolfman can then update his code,
commit locally,
and push those changes to GitHub
to update the pull request:

FIXME: diagram

This process is exactly like peer review of papers,
though usually much faster.
In large open source projects like Firefox,
it's very common for a pull request to be updated several times
before finally being accepted and merged.
Working this way not only helps maintain the quality of the code,
it is also a very effective way to transfer knowledge.

What happens if Wolfman wants to do more work
while he's waiting for Dracula to review his first modification?
Simple:
he creates a new branch in his local repository,
pushes it to GitHub,
and then issues a pull request from that:

FIXME: diagram

We can now see why Git, Mercurial, and other modern version control systems
use branching so much:
it helps people work concurrently but asynchronously,
i.e.,
in parallel but on their own time.
It might take Dracula several days to get around to reviewing Wolfman's changes.
Rather than being stalled until then,
Wolfman can just switch to another branch and work on something else,
then switch back when Dracula's review finally comes in.
Once the changes in a particular branch have been accepted,
Wolfman can delete it;
provided it has been merged into `master` (or some other branch),
the only thing that will be lost is the pointer with the branch name,
not the changes themselves.

We said above that code review is
half the reason every developer should have their own repository on GitHub
(or whatever service is being used).
The other reason is that working this way allows people to explore ideas
without needing permission from any central authority.
If you want to change this tutorial,
you can fork the Software Carpentry repository on GitHub
and start rewriting things.
If you think we might prefer your version to ours,
you can send us a pull request,
but you don't have to.
If other people like your version better than ours,
they can start forking your repository
and sending pull requests to you instead of to us.

If this sounds familiar,
it's because it is the way science itself works.
When someone publishes a new method or result,
other scientists can immediately start building on top of it---essentially,
they can create their own fork of the work
and start committing changes to it.
If the first scientist likes the second's work,
she can incorporate those findings into her next paper,
which is analogous to merging a pull request.
If she doesn't,
then it's up to other scientists to decide whose work to build on,
or whether to try to combine both approaches.

## The Opposite of "Open" Isn't "Closed", It's "Broken"

Free sharing of information might be the ideal in science,
but the reality is often more complicated.
Normal practice today looks something like this:

* A scientist collects some data and stores it on a machine
  that is occasionally backed up by her department.
* She then writes or modifies a few small programs
  (which also reside on her machine)
  to analyze that data.
* Once she has some results,
  she writes them up and submits her paper.
  She might include her data---a growing number of journals require this---but
  she probably doesn't include her code.
* Time passes.
* The journal sends her reviews written anonymously by a handful of other people in her field.
  She revises her paper to satisfy them,
  during which time she might also modify the scripts she wrote earlier,
  and resubmits.
* More time passes.
* The paper is eventually published.
  It might include a link to an online copy of her data,
  but the paper itself will be behind a paywall:
  only people who have personal or institutional access
  will be able to read it.

For a growing number of scientists,
though,
the process looks like this:

* The data that the scientist collects is stored in an open access repository
  like [figshare](http://figshare.com/) or [Dryad](http://datadryad.org/)
  as soon as it's collected,
  and given its own DOI.
* The scientist creates a new repository on GitHub to hold her work.
* As she does her analysis,
  she pushes changes to her scripts
  (and possibly some output files)
  to that repository.
  She also uses the repository for her paper;
  that repository is then the hub for collaboration with her colleagues.
* When she's happy with the state of her paper,
  she posts a version to [arXiv](http://arxiv.org/)
  or some other preprint server
  to invite feedback from peers.
* Based on that feedback,
  she may post several revisions
  before finally submitting her paper to a journal.
* The published paper includes links to her preprint
  and to her code and data repositories,
  which  makes it much easier for other scientists
  to use her work as starting point for their own research.

Studies have shown that the more open model accelerates discovery,
and that more open work is more widely cited.
However,
people who want to work this way need to make some decisions
about what exactly "open" means in practice.

### Licensing

The first question is licensing.
Broadly speaking,
there are two kinds of open license for software,
and half a dozen for data and publications.
For software,
people can choose between the [GNU Public License](http://opensource.org/licenses/GPL-3.0) (GPL) on the one hand,
and licenses like the [MIT](http://opensource.org/licenses/MIT)
and [BSD](http://opensource.org/licenses/BSD-2-Clause) licenses on the other.
All of these licenses allow unrestricted sharing and modification of programs,
but the GPL is [infective](glossary.html#infective_license):
anyone who distributes a modified version of the code
(or anything that includes GPL'd code)
must make *their* code freely available as well.

Proponents of the GPL argue that this requirement is needed
to ensure that people who are benefiting from freely-available code
are also contributing back to the community.
Opponents counter that many open source projects have had long and successful lives
without this condition,
and that the GPL makes it more difficult to combine code from different sources.
At the end of the day,
what matters most is that:

1. every project have a file in its home directory
   called something like `LICENSE` or `LICENSE.txt`
   that clearly states what the license is, and
2. people use existing licenses rather than writing new ones.

The second of these points is as important as the first:
most scientists are not lawyers,
so wording that may seem sensible to a layperson
may have unintended gaps or consequences.
The [Open Source Initiative](http://opensource.org/)
maintains a list of open source licenses,
and [tl;drLegal](http://www.tldrlegal.com/) explains most of them in plain English.

When it comes to data, publications, and other "static" material,
scientists have many more options to choose from.
The good news is that an organization called [Creative Commons(http://creativecommons.org/)
has prepared a set of licenses using combinations of four basic restrictions:

* Attribution: derived works must give the original author credit for their work.
* No Derivatives: people may copy the work, but must pass it along unchanged.
* Share Alike: derivative works must license their work under the same terms as the original.
* Noncommercial: free use is allowed, but commercial use is not.

These four restrictions are abbreviated "BY", "ND", "SA", and "NC" respectively,
so "CC-BY-ND" means,
"People can re-use the work both for free and commercially,
but cannot make changes and must cite the original."
These [short descriptions](http://creativecommons.org/licenses/)
summarize the six CC licenses in plain language,
and include links to their full legal formulations.

There is one other important license that doesn't fit into this categorization.
Scientists (and other people) can choose to put material in the public domain,
which is often abbreviated "PD".
In this case,
anyone can do anything they want with it,
without needing to cite the original
or restrict further re-use.
The table below shows how the six Creative Commons licenses and PD relate to one another:

<table border="1">
  <tr>
    <td></td>
    <td colspan="7" align="center">Licenses that can be used for derivative work or adaptation</td>
  </tr>
  <tr>
    <td>Original work</td> <td>by</td> <td>by-nc</td> <td>by-nc-nd</td> <td>by-nc-sa</td> <td>by-nd</td> <td>by-sa</td> <td>pd</td>
  </tr>
  <tr>
    <td>by</td>       <td>X</td> <td>X</td> <td>X</td> <td>X</td> <td>X</td> <td>X</td> <td> </td>
  </tr>
  <tr>
    <td>by-nc</td>    <td> </td> <td>X</td> <td>X</td> <td>X</td> <td> </td> <td> </td> <td> </td>
  </tr>
  <tr>
    <td>by-nc-nd</td> <td> </td> <td> </td> <td> </td> <td> </td> <td> </td> <td> </td> <td> </td>
  </tr>
  <tr>
    <td>by-nc-sa</td> <td> </td> <td> </td> <td> </td> <td>X</td> <td> </td> <td> </td> <td> </td>
  </tr>
  <tr>
    <td>by-nd</td>    <td> </td> <td> </td> <td> </td> <td> </td> <td> </td> <td> </td> <td> </td>
  </tr>
  <tr>
    <td>by-sa</td>    <td> </td> <td> </td> <td> </td> <td> </td> <td> </td> <td>X</td> <td> </td>
  </tr>
  <tr>
    <td>pd</td>       <td>X</td> <td>X</td> <td>X</td> <td>X</td> <td>X</td> <td>X</td> <td>X</td>
  </tr>
</table>

[Software Carpentry](http://software-carpentry.org/license.html)
uses CC-BY for its lessons and the MIT License for its code
in order to encourage the widest possible re-use.
Again,
the most important thing is for the `LICENSE` file in the root directory of your project
to state clearly what your license is.
You may also want to include a file called `CITATION` or `CITATION.txt`
that describes how to reference your project;
the one for Software Carpentry states:

    To reference Software Carpentry in publications, please cite both of the following:

    Greg Wilson: "Software Carpentry: Getting Scientists to Write Better
    Code by Making Them More Productive".  Computing in Science &
    Engineering, Nov-Dec 2006.

    Greg Wilson: "Software Carpentry: Lessons Learned". arXiv:1307.5448,
    July 2013.

    @article{wilson-software-carpentry-2006,
        author =  {Greg Wilson},
        title =   {Software Carpentry: Getting Scientists to Write Better Code by Making Them More Productive},
        journal = {Computing in Science \& Engineering},
        month =   {November--December},
        year =    {2006},
    }

    @online{wilson-software-carpentry-2013,
      author      = {Greg Wilson},
      title       = {Software Carpentry: Lessons Learned},
      version     = {1},
      date        = {2013-07-20},
      eprinttype  = {arxiv},
      eprint      = {1307.5448}
    }


### Hosting

The second big question for groups that want to open up their work
is where to host their code and data.
One option is for the lab, the department, or the university to provide a server,
manage accounts and backups,
and so on.
The main benefit of this is that it clarifies who owns what,
which is particularly important if any of the material is sensitive
(i.e.,
relates to experiments involving human subjects
or may be used in a patent application).
The main drawbacks are the cost of providing the service and its longevity:
a scientist who has spent ten years collecting data
would like to be sure that data will still be available ten years from now,
but that's well beyond the lifespan of most of the grants that fund academic infrastructure.

The alternative is to use a public hosting service like [GitHub](http://github.com),
[BitBucket](http://bitbucket.org),
[Google Code](http://code.google.com),
or [SourceForge](http://sourceforge.net).
All of these allow people to create repositories through a web interface,
and also provide mailing lists,
ways to keep track of who's doing what,
and so on.
They all benefit from economies of scale and network effects:
it's easier to run one large service well
than to run many smaller services to the same standard,
and it's also easier for people to collaborate if they're using the same service,
not least because it gives them fewer passwords to remember.

However,
all of these services place some constraints on people's work.
In particular,
they give users a choice:
if they're willing to share their work with others,
it will be hosted for free,
but if they want privacy,
they have to pay.
Sharing might seem like the only valid choice for science,
but many institutions may not allow researchers to do this,
either because they want to protect future patent applications
or simply because what's new is often also frightening.

### Get the Facts

Most students don't actually know who owns their work.
Does it belong to the university?
To their supervisor?
Can they take their work with them if they leave the university,
or did something in the fine print of the registration forms they signed without reading
hand that to someone else?

Most faculty and administrators don't actually know either.
Instead,
they half-remember what the rules were five or ten years ago,
but haven't kept up with changes made since.
As a result,
many research projects are open sourced by fiat:
a student or faculty member declares that the work is covered by a particular license,
puts it into a public repository,
and waits for someone to object.

This approach has worked surprisingly well so far,
but we still suggest that people ask someone from their institution's intellectual property office
to give a lunchtime talk on these issues
*before* deciding what to do and how to do it:
It's clear that tomorrow's science and scientific computing will be more open than yesterday's,
and that this will benefit everyone,
but the fewer stumbles we make along the way,
the faster we'll get there.

## git merge : Conflicts

This is the trickiest part of version control, so let's take it very
carefully.

In the YYYY-MM-PLACE code, you'll find a file called Readme.md. This is a
standard documentation file that appears rendered on the landing page
for the repository in github. To see the rendered version, visit your
fork on github, (https://github.com/YOU/boot-camps/tree/YYYY-MM-PLACE/README.md).

For illustration, let's imagine that, suddenly, each of the developers
on the YYYY-MM-PLACE code would like to welcome visitors in a language other
than English. Since we're all from so many different places and speak
so many languages, there will certainly be disagreements about what to
say instead of "Welcome."

I, for example, am from Tamil Nadu, India, so I'll push (to the upstream
repository) my own version of Welcome on line 5 of Readme.md.

You may speak another language, perhaps even English, however, and may want
to replace the Tamil word 'vanakkam' with an equivalent word that you
prefer (welcome, willkommen, bienvenido, benvenuti, etc.).

You'll want to start a new branch for development. It's a good convention
to think of your master branch (in this case your YYYY-MM-PLACE branch) as
the "production branch," typically by keeping that branch clean of your
local edits until they are ready for release. Developers typically use the
master branch of their local fork to track other developers changes in the
remote repository until their own local development branch changes are
ready for production.

### Exercise : Experience a Conflict

Step 1 : Make a new branch, edit the readme file in that branch, and
commit your changes.

    $ git branch development
    $ git checkout development
    Switched to branch 'development'
    $ kate Readme.md &
    <edit the readme file and exit kate>
    $ git commit -am "Changed the welcome message to ... "

Step 2 : Mirror the remote upstream repository in your master branch (in
this case your YYYY-MM-PLACE branch) by pulling down my changes

    $ git checkout YYYY-MM-PLACE
    Switched to branch 'YYYY-MM-PLACE'
    $ git fetch upstream
    $ git merge upstream/YYYY-MM-PLACE
    Updating 43844ea..3b36a87
    Fast-forward
     README.rst |   2 +-
     1 files changed, 1 insertions(+), 1 deletions(-)

Step 3 : You want to push it to the internet eventually, so you pull
updates from the upstream repository, but will experience a conflict.

    $ git merge development
    Auto-merging Readme.md
    CONFLICT (content): Merge conflict in Readme.md
    Automatic merge failed; fix conflicts and then commit the result.

## git resolve : Resolving Conflicts

Now what?

Git has paused the merge. You can see this with the **git status**
command.

    # On branch YYYY-MM-PLACE
    # Unmerged paths:
    #   (use "git add/rm <file>..." as appropriate to mark resolution)
    #
    #       unmerged:      Readme.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")

The only thing that has changed is the Readme.md file. Opening it,
you'll see something like this at the beginning of the file.

    =====================
    <<<<<<< HEAD
    Vanakkam
    =======
    Willkommen
    >>>>>>> development
    =====================

The intent is for you to edit the file, knowing now that I wanted the
Welcome to say Vanakkam. If you want it to say Willkommen, you should
delete the other lines. However, if you want to be inclusive, you may
want to change it to read Vanakkam and Willkommen. Decisions such as this
one must be made by a human, and why conflict resolution is not handled
more automatically by the version control system.

    Vanakkam and Willkommen

This results in a status To alert git that you have made appropriate
alterations,

    $ git add Readme.md
    $ git commit
    Merge branch 'development'

    Conflicts:
      Readme.md
    #
    # It looks like you may be committing a MERGE.
    # If this is not correct, please remove the file
    # .git/MERGE_HEAD
    # and try again.
    #
    $ git push origin YYYY-MM-PLACE
    Counting objects: 10, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 762 bytes, done.
    Total 6 (delta 2), reused 0 (delta 0)
    To git@github.com:username/boot-camps.git
