

#To-do:
- exercises
- git hub 
- git fetch+merge vs. pull
- make sure they are signed up for github.
- first create their own repo on github (and put their files from yesterday in it?) and then clone ours with some files to work on, or should we just be confident that they will go with it?
- 

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
https://github.com/

then go to a button up at the top right corner next to your name and click on the button to create a new repo. 

You are the owner and give the repository a name appropriate for the work you want to put in it. 

Make it a private repo and yes initialize with a readme. Do not add a .gitignore or a license. Create the repository. 

This effectively does the following on GitHub's servers:

```
$ mkdir planets
$ cd planets
$ git init
```

We're now in the situation shown in the figure below:

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
find this: https://github.com/jooolia/Thesis-Public.git

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


#If I do this example I would have to tell students not to follow along for a minute or so. Or maybe I should just move this section. 
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

```
Show on web browser
```

He then clones his GitHub repository,
not Dracula's,
to give himself a desktop copy:


This may seem like unnecessary work,
but it allows Wolfman and Dracula to collaborate much more effectively.
Suppose Wolfman makes a change to the project.
He commits it to his local repository,
then uses `git push` to copy those changes to GitHub:

He then creates a [pull request](glossary.html#pull_request),
which notifies Dracula that Wolfman wants to merge some changes
into Dracula's repository:


A pull request is a merge waiting to happen.
When Dracula views it online,
he can see and comment on the changes Wolfman wants to make:


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

I see that github has a new feature where you can merge pull requests on your cell phone now. 

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

- practice this a few times. 
- or could we get them to make repos with their neighbours to practice working as a small team and then making conflicts?
## Now we're ready to try it with some data we want to use later on. 
- Now we fork the repo that Doug and I have designed that has a few scripts (note that you can only have 1 fork of a repo).
- Paste address into etherpad
- Make sure to be logged in. Click the fork button.
- Clone your fork to you computer:
```
git clone git@github.com:your-user-name/UBC_bootcamp_repo.git
cd UBC_bootcamp_repo
git remote add upstream git://github.com/DougLatornell/UBC_bootcamp_repo.git
- Add upstream remotes 

Then type:
```
git branch -a
```

to show you all branches. You’ll get something like:
```
* master
remotes/origin/master
```

- Add some observations to file x
- change them. 
- pull requests to the repo to submit their file. 
(based on Everyone will have a CSV file containing hourly data for the entire month of August 2013 at YVR. One day's worth of the data can be seen here: 
http://climate.weather.gc.ca/climateData/hourlydata_e.html?timeframe=1&Prov=&StationID=51442&hlyRange=2013-06-11|2013-09-12&cmdB1=Go&cmdB2=Go&Year=2013&Month=8&Day=30

Each person will also have daily data for an entire year at Point Atkinson. One month's worth of the data can be seen at http://climate.weather.gc.ca/climateData/dailydata_e.html?timeframe=2&Prov=BC&StationID=844&dlyRange=1968-01-01|2013-09-16&Year=2012&Month=11&Day=01

)
# will they be named differently?
Then goal is to have 25 similar daily datasets that can be iterated over in the automation part. 