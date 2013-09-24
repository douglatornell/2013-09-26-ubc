#Shell

### TO DO: ###
- add more about regular expressions (?)
- add commands about history
- add command using less
- make example using grep and outputting output that way. 
- cheat sheet
- git bash quirks, does not allow you to paste from the mouse, need to go into the menu bar
- insert exercises in appropriate spots
- is there an interesting file to do some of these exercises with wc and stuff with?


 Many people have questioned whether we should still teach the shell. After all, anyone who wants to rename several thousand data files can easily do so interactively in the Python interpreter, and anyone who's doing serious data analysis is probably going to do most of their work inside the IPython Notebook or R Studio. So why teach the shell?

The first answer is,"Because so much else depends on it. Installing software, configuring your default editor, and controlling remote machines frequently assume a basic familiarity with the shell, and with related ideas like standard input and output. Many tools also use its terminology (for example,the <code>%ls</code> and <code>%cd</code> magic commands in IPython).

The second answer is, "Because it's an easy way to introduce some fundamental ideas about how to use computers." As we teach people how to use the Unix shell, we teach them that they should get the computer to repeat things(via tab completion,<code>!</code> followed by a command number, and <code>for</code> loops) rather than repeating things themselves. We also teach them to take things they've discovered they do frequently and save them for later re-use(via shell scripts),to give things sensible names,and to write a little bit of documentation(like comment at the top of shell scripts)to make their future selves' lives better.

Finally, and perhaps most importantly, teaching people the shell lets us teach them to think about programming in terms of function composition. In the case of the shell, this takes the form of pipelines rather than nested function calls, but the core idea of "small pieces, loosely joined" is the same.

 Here are some ways to approach this material:

- Have learners open a shell and then do `whoami`, <code>pwd</code>, and <code>ls</code>.
- Then have them create a directory called <code>bootcamp</code> and <code>cd</code> into it, so that everything else they do during the lesson is unlikely to harm whatever files they already have.
- Get them to run an editor and save a file in their <code>bootcamp</code> directory as early as possible. Doing this is usually the biggest stumbling block during the entire lesson: many will try to run the same editor as the instructor (which may leave them trapped in the awful nether hell that is Vim), or will not know how to navigate to the right directory to save their file, or will run a word processor rather than a plain text editor. The quickest way past these problems is to have more knowledgeable learners help those who need it.

Tab completion sounds like a small thing: it isn't.Re-running old commands using <code>!123</code> or <code>!wc</code>isn't a small thing either, and neither are wildcard expansion and <code>for</code> loops Each one is an opportunity to repeat one of the big ideas of Software Carpentry: if the computer <em>can</em> repeat it, some programmer somewhere will almost certainly have built some way for the computer <em>to</em> repeat it.

Building up a pipeline with four or five stages, then putting it in a shell script for re-use and calling that script inside a <code>for</code> loop, is a great opportunity to show how  "seven plus or minus two" connects to programming. Once we have figured out how to do something moderately complicated, we make it re-usable and give it a name so that it only takes up one slot in working memory rather than several. It is also a good opportunity to talk about exploratory programming: rather than designing a program up front, we can do a few useful things and then retroactively decide which are worth encapsulating for future re-use.


## Intro to command prompt ##


### Objectives ###

- Explain the similarities and differences between a file and a directory.
- Translate an absolute path into a relative path and vice versa.
- Construct absolute and relative paths that identify specific files and directories.
- Explain the steps in the shell's read-run-print cycle.
- Identify the actual command, flags, and filenames in a command-line call.
- Demonstrate the use of tab completion, and explain its advantages.

Duration: 15 minutes (longer if people have trouble getting an editor to work).



The part of the operating system responsible for managing files and directories is called the file system. It organizes our data into files, which hold information, and directories (also called "folders"), which hold files or other directories.

Several commands are frequently used to create, inspect, rename, and delete files and directories. To start exploring them, let's log in to the computer by typing our user ID and password. Most systems will print stars to obscure the password, or nothing at all, in case some evildoer is shoulder surfing behind us.

    login: Julia
    password: ********
    $

Once we have logged in we'll see a prompt, which is how the shell tells us that it's waiting for input. This is usually just a dollar sign, but which may show extra information such as our user ID or the current time. Type the command `whoami`, then press the Enter key (sometimes marked Return) to send the command to the shell. The command's output is the ID of the current user, i.e., it shows us who the shell thinks we are:

    $ whoami
    Julia
    $

More specifically, when we type whoami the shell:

- finds a program called whoami,
- runs it,
- waits for it to display its output, and
-displays a new prompt to tell us that it's ready for more commands.

Next, let's find out where we are by running a command called `pwd` (which stands for "print working directory"). At any moment, our current working directory is our current default directory, i.e., the directory that the computer assumes we want to run commands in unless we explicitly specify something else. Here, the computer's response is /users/Julia, which is Vlad's home directory:

    $ pwd
    /users/Julia
    $

Alphabet Soup

If the command to find out who we are is `whoami`, the command to find out where we are ought to be called `whereami`, so why is it `pwd` instead? The usual answer is that in the early 1970s, when Unix was first being developed, every keystroke counted: the devices of the day were slow, and backspacing on a teletype was so painful that cutting the number of keystrokes in order to cut the number of typing mistakes was actually a win for usability. The reality is that commands were added to Unix one by one, without any master plan, by people who were immersed in its jargon. The result is as inconsistent as the roolz uv Inglish speling, but we're stuck with it now.

To understand what a "home directory" is, let's have a look at how the file system as a whole is organized (Figure 4). At the top is the root directory that holds everything else the computer is storing. We refer to it using a slash character / on its own; this is the leading slash in /users/Julia.
File System Figure 4: File System

Inside that directory (or underneath it, if you're drawing a tree) are several other directories: bin (which is where some built-in programs are stored), data (for miscellaneous data files), users (where users' personal directories are located), tmp (for temporary files that don't need to be stored long-term), and so on. We know that our current working directory /users/Julia is stored inside /users because /users is the first part of its name. Similarly, we know that /users is stored inside the root directory / because its name begins with /.

Underneath /users, we find one directory for each user with an account on this machine (Figure 5). The Mummy's files are stored in /users/imhotep, Wolfman's in /users/larry, and ours in /users/Julia, which is why Julia is the last part of the directory's name. Notice, by the way, that there are two meanings for the / character. When it appears at the front of a file or directory name, it refers to the root directory. When it appears inside a name, it's just a separator.
Home Directories Figure 5: Home Directories

Let's see what's in Vlad's home directory by running ls, which stands for "listing":

    $ ls
    bin  data  mail   music
    notes.txtpaperspizza.cfg  solar
    solar.pdfswc
    $

`ls` prints the names of the files and directories in the current directory in alphabetical order, arranged neatly into columns. To make its output more comprehensible, we can give it the flag -F by typing `ls -F`. This tells ls to add a trailing / to the names of directories:

$ ls -F
bin/ data/ mail/  music/
notes.txtpapers/   pizza.cfg  solar/
solar.pdfswc/
$

As you can see, /users/Julia contains seven sub-directories (Figure 6). The names that don't have trailing slashes—notes.txt, pizza.cfg, and solar.pdf—are plain old files.
Vlad's Home Directory Figure 6: Vlad's Home Directory
What's In A Name?

You may have noticed that all of Vlad's files' names are "something dot something". This is just a convention: we can call a file mythesis or almost anything else we want. However, most people use two-part names most of the time to help them (and their programs) tell different kinds of files apart. The second part of such a name is called the filename extension, and indicates what type of data the file holds: .txt signals a plain text file, .pdf indicates a PDF document, .cfg is a configuration file full of parameters for some program or other, and so on.

It's important to remember that this is just a convention. Files contain bytes: it's up to us and our programs to interpret those bytes according to the rules for PDF documents, images, and so on. For example, naming a PNG image of a whale as whale.mp3 doesn't somehow magically turn it into a recording of whalesong.

Now let's take a look at what's in Vlad's data directory by running the command `ls -F` data. The second parameter—the one without a leading dash—tells ls that we want a listing of something other than our current working directory:

    $ ls -F data
    amino_acids.txt   elements/ morse.txt
    pdb/  planets.txt   sunspot.txt
    $

The output shows us that there are four text files and two sub-sub-directories. Organizing things hierarchically in this way is a good way to keep track of our work: it's possible to put hundreds of files in our home directory, just as it's possible to pile hundreds of printed papers on our desk, but in the long run it's a self-defeating strategy.

Notice, by the way that we spelled the directory name data. It doesn't have a trailing slash: that's added to directory names by ls when we use the -F flag to help us tell things apart. And it doesn't begin with a slash because it's a relative path, i.e., it tells ls how to find something from where we are, rather than from the root of the file system (Figure 7).
Absolute and Relative Paths Figure 7: Absolute and Relative Paths

If we run `ls -F /data` (with a leading slash) we get a different answer, because /data is an absolute path:

    $ ls -F /data
    access.logbackup/hardware.cfg
    network.cfg
    $

The leading `/` tells the computer to follow the path from the root of the filesystem, so it always refers to exactly one directory, no matter where we are when we run the command.

What if we want to change our current working directory? Before we do this, `pwd` shows us that we're in /users/Julia, and ls without any parameters shows us that directory's contents:

    $ pwd
    /users/Julia
    $ ls
    bin/ data/ mail/  music/
    notes.txtpapers/   pizza.cfg  solar/
    solar.pdfswc/
    $

We can use cd followed by a directory name to change our working directory. cd stands for "change directory", which is a bit misleading: the command doesn't change the directory, it changes the shell's idea of what directory we are in.

    $ cd data
    $

cd doesn't print anything, but if we run `pwd` after it, we can see that we are now in /users/Julia/data. If we run ls without parameters now, it lists the contents of /users/Julia/data, because that's where we now are:

    $ pwd
    /users/Julia/data
    $ ls
    amino_acids.txt   elements/ morse.txt
    pdb/  planets.txt   sunspot.txt
    $
    
OK, we can go down the directory tree: how do we go up? We could use an absolute path:

    $ cd /users/Julia
    $

but it's almost always simpler to use cd .. to go up one level:

    $ pwd
    /users/Julia/data
    $ cd ..

.. is a special directory name meaning "the directory containing this one", or, more succinctly, the parent of the current directory. Sure enough, if we run pwd after running cd .., we're back in /users/Julia:

    $ pwd
    /users/Julia
    $

The special directory .. doesn't usually show up when we run ls. If we want to display it, we can give ls the -a flag:

    $ ls -F -a
    ./   ../   bin/   data/
    mail/music/notes.txt  papers/
    pizza.cfgsolar/solar.pdfswc/
    
-a stands for "show all"; it forces `ls` to show us file and directory names that begin with ., such as .. (which, if we're in /users/Julia, refers to the /users directory). As you can see, it also displays another special directory that's just called ., which means "the current working directory". It may seem redundant to have a name for it, but we'll see some uses for it soon.
Orthogonality

The special names . and .. don't belong to ls; they are interpreted the same way by every program. For example, if we are in /users/Julia/data, the command ls .. will give us a listing of /users/Julia. Programmers call this orthogonality: the meanings of the parts are the same no matter how they're combined. Orthogonal systems tend to be easier for people to learn because there are fewer special cases and exceptions to keep track of.

Everything we have seen so far works on Unix and its descendents, such as Linux and Mac OS X. Things are a bit different on Windows. A typical directory path on a Windows 7 machine might be C:\Users\Julia. The first part, C:, is a drive letter that identifies which disk we're talking about. This notation dates back to the days of floppy drives; today, different "drives" are usually different filesystems on the network.

Instead of a forward slash, Windows uses a backslash to separate the names in a path. This causes headaches because Unix uses backslash for input of special characters. For example, if we want to put a space in a filename on Unix, we would write the filename as my\ results.txt. Please don't ever do this, though: if you put spaces, question marks, and other special characters in filenames on Unix, you can confuse the shell for reasons that we'll see shortly.

Finally, Windows filenames and directory names are case insensitive: upper and lower case letters mean the same thing. This means that the path name C:\Users\Julia could be spelled c:\users\JULIA, C:\Users\julia, and so on. Some people argue that this is more natural: after all, "JULIA" in all upper case and "Julia" spelled normally refer to the same person. However, it causes headaches for programmers, and can be difficult for people to understand if their first language doesn't use a cased alphabet.


### Exercises ###
#### Exercise 1 ####

 What does the command cd without a directory name do?

1. It has no effect.
1. It changes the working directory to /.
1. It changes the working directory to the user's home directory.
1. It is an error.

#### Exercise 2 ####
We said earlier that spaces in path names have to be marked with a leading backslash in order for the shell to interpret them properly. Why? What happens if we run a command like:

    $ ls my\ thesis\ files

without the backslashes? 


# Creating files #

## Objectives ##

- Create a directory hierarchy that matches a given diagram.
- Create files in that hierarchy using an editor or by copying and renaming existing files.
- Display the contents of a directory using the command line.
- Delete specified files and/or directories.

### Duration: 10 minutes.


We now know how to explore files and directories, but how do we create them in the first place? Let's go back to Julia's home directory, /users/Julia, and use `ls -F` to see what it contains:

$ pwd
/users/Julia
$ ls -F
bin/ data/ mail/  music/
notes.txtpapers/   pizza.cfg  solar/
solar.pdfswc/
$

Let's create a new directory called thesis using the command `mkdir thesis` (which has no output):

    $ mkdir thesis
    $
    
As you might (or might not) guess from its name, `mkdir` means "make directory". Since thesis is a relative path (i.e., doesn't have a leading slash), the new directory is made below the current one:

    $ ls -F
    bin/ data/ mail/  music/
    notes.txtpapers/   pizza.cfg  solar/
    solar.pdfswc/  thesis/
    $
    
However, there's nothing in it yet:

    $ ls -F thesis
    $
    
Let's change our working directory to thesis using `cd`, then run an editor called Nano to create a file called `nano draft.txt`:

    $ cd thesis
    $ nano draft.txt

Nano is a very simple text editor that only a programmer could really love. Figure 9 shows what it looks like when it runs: the cursor is the blinking square in the upper left, and the two lines across the bottom show us the available commands. (By convention, Unix documentation uses the caret ^ followed by a letter to mean "control plus that letter", so ^O means Control+O.)


Let's type in a short quotation(FIXME!!!) then use Control-O to write our data to disk. Once our quotation is saved, we can use Control-X to quit the editor and return to the shell.


		Student exercise: Make a new directory and make a new file. Check that it is present. Check the content. (list the step. 

		#type in your data and then to save you hit Ctl-O (^ caret is used for ctrl (I used to think it was carrot thinking it was an upside down carrot))
		
		Save by hitting Ctrl O and then Ctrl -X to exit. 
		
#### Which Editor? ####

When we say, "nano is a text editor," we really do mean "text": it can only work with plain character data, not tables, images, or any other human-friendly media. We use it in examples because almost anyone can drive it anywhere without training, but please use something more powerful for real work. On Unix systems (such as Linux and Mac OS X), many programmers use Emacs or Vim (both of which are completely unintuitive, even by Unix standards), or a graphical editor such as Gedit. On Windows, you may wish to use Notepad++.

No matter what editor you use, you will need to know where it searches for and saves files. If you start it from the shell, it will (probably) use your current working directory as its default location. If you use your computer's start menu, it may want to save files in your desktop or documents directory instead. You can change this by navigating to another directory the first time you "Save As..."

nano doesn't leave any output on the screen after it exits. But ls now shows that we have created a file called draft.txt:

    $ ls
    draft.txt
    $

We can run `ls` with the `-s` flag (for "size") to show us how large draft.txt is:

    $ ls -s
       1  draft.txt
    $
    
Unfortunately, Unix reports sizes in disk blocks by default, which might be the least helpful default imaginable. If we add the -h flag, ls switches to more human-friendly units:

    $ ls -s -h
     512  draft.txt
    $

Here, 512 is the number of bytes in the file. This is more than we actually typed in because the smallest unit of storage on the disk is typically a block of 512 bytes.

		ls 
		Ok we're in the directory. How does we find out what is here? Type this command to list all files in directory. 
		 
		If we need to see hidden files or directories we can type ls -a "list all"
		
		ls -la  # long all

Let's tidy up by running rm draft.txt:

    $ rm draft.txt
    $
    
This command removes files ("rm" is short for "remove"). If we now run ls again, its output is empty once more, which tells us that our file is gone:

    $ ls
    $
    
Deleting Is Forever

Unix doesn't have a trash bin: when we delete files, they are unhooked from the file system so that their storage space on disk can be recycled. Tools for finding and recovering deleted files do exist, but there's no guarantee they'll work in any particular situation, since the computer may recycle the file's disk space right away.

Let's re-create that file and then move up one directory to /users/Julia using `cd ..`:

    $ pwd
    /users/Julia/thesis
    $ nano draft.txt
    $ ls
    draft.txt
    $ cd ..
    $
    
If we try to remove the entire thesis directory using rm thesis, we get an error message:

    $ rm thesis
    rm: cannot remove `thesis': Is a directory
    $

This happens because rm only works on files, not directories. The right command is `rmdir`, which is short for "remove directory": It doesn't work yet either, though, because the directory we're trying to remove isn't empty:

    $ rmdir thesis
    rmdir: failed to remove `thesis': Directory not empty
    $

This little safety feature can save you a lot of grief, particularly if you are a bad typist. If we really want to get rid of thesis we should first delete the file draft.txt:

    $ rm thesis/draft.txt
    $

The directory is now empty, so rmdir can delete it:

    $ rmdir thesis
    $

#### With Great Power Comes Great Responsibility ####

Removing the files in a directory just so that we can remove the directory quickly becomes tedious. Instead, we can use rm with the -r flag (which stands for "recursive"):

    $ rm -r thesis
    $

This removes everything in the directory, then the directory itself. If the directory contains sub-directories, `rm -r` does the same thing to them, and so on. It's very handy, but can do a lot of damage if used without care.

Let's create that directory and file one more time. (Note that this time we're running nano with the path thesis/draft.txt, rather than going into the thesis directory and running nano on draft.txt there.)

    $ pwd
    /users/Julia/
    $ mkdir thesis
    $ nano thesis/draft.txt
    $ ls thesis
    draft.txt
    $
    
draft.txt isn't a particularly informative name, so let's change the file's name using mv, which is short for "move":

    $ mv thesis/draft.txt thesis/quotes.txt
    $

The first parameter tells mv what we're "moving", while the second is where it's to go. In this case, we're moving thesis/draft.txt to thesis/quotes.txt, which has the same effect as renaming the file. Sure enough, ls shows us that thesis now contains one file called quotes.txt:

    $ ls thesis
    quotes.txt
    $

Just for the sake of inconsistency, mv also works on directories—there is no separate mvdir command.

Let's move quotes.txt into the current working directory. We use mv once again, but this time we'll just use the name of a directory as the second parameter to tell mv that we want to keep the filename, but put the file somewhere new. (This is why the command is called "move".) In this case, the directory name we use is the special directory name . that we mentioned earlier):

    $ mv thesis/quotes.txt .
    $

The effect is to move the file from the directory it was in to the current directory. ls now shows us that thesis is empty, and that quotes.txt is in our current directory:

    $ ls thesis
    $ ls quotes.txt
    quotes.txt
    $

(Notice that ls with a filename or directory name as an parameter only lists that file or directory.)

The `cp` command works very much like `mv`, except it copies a file instead of moving it. We can check that it did the right thing using ls with two paths as parameters—like most Unix commands, ls can be given thousands of paths at once:

    $ cp quotes.txt thesis/quotations.txt
    $ ls quotes.txt thesis/quotations.txt
    quotes.txt   thesis/quotations.txt
    $

To prove that we made a copy, let's delete the quotes.txt file in the current directory, and then run that same ls again. This time, it tells us that it can't find quotes.txt in the current directory, but it does find the copy in thesis that we didn't delete:

    $ ls quotes.txt thesis/quotations.txt
    ls: cannot access quotes.txt: No such file or directory
    thesis/quotations.txt
    $

#### Another Useful Abbreviation ####

The shell interprets the character `~` (tilde) at the start of a path to mean "the current user's home directory". For example, if Julia's home directory is /home/Julia, then ~/data is equivalent to /home/Julia/data. This only works if it is the first character in the path: /~ is not the user's home directory, and here/there/~/elsewhere is not /home/Julia/elsewhere.


### Exercises ###

#### Exercise 1 ####
 Suppose that:

    $ ls -F
    analyzed/  fructose.datraw/   sucrose.dat

What command(s) could you run so that the commands below will produce the output shown?

    $ ls
    analyzed   raw
    $ ls analyzed
    fructose.datsucrose.dat

#### Exercise 2 ####

 What does cp do when given several filenames and a directory name, as in:
    
    $ mkdir backup
    $ cp thesis/citations.txt thesis/quotations.txt backup

What does cp do when given three or more filenames, as in:

$ ls -F
intro.txtmethods.txtsurvey.txt
$ cp intro.txt methods.txt survey.txt

Why do you think cp's behavior is different from mv's?

#### Exercise 3 ####

 What is the output of the closing ls command in the sequence shown below?

    $ pwd
    /home/thing/data
    $ ls
    proteins.dat
    $ mkdir recombine
    $ mv proteins.dat recombine
    $ cp recombine/proteins.dat ../proteins-saved.dat
    $ ls

### Exercise 4 ###

The command `ls -R` lists the contents of directories recursively, i.e., lists their sub-directories, sub-sub-directories, and so on in alphabetical order at each level. The command `ls -t` lists things by time of last change, with most recently changed files or directories first. In what order does `ls -R -t` display things? 


### Exercise 5 ### 

Make a new file called "temperature_observations.txt".
In it write the date in ISo format- 2013-09-24 and and space and the temperature for the last 3 days. 
Save file.
copy this file to thesis/observations

		
	Dealing with data in a file
	Purpose: Slicing and dicing data from one and multiple data files
	Student exercises: Sort abundance file and print highest abundance to new file, loop over multiple files and keep highest  abundance.
	
	Create file with names (date, species, abundance)
	(have draft of what I want it to look like---mammals we see at UW)
	nano  mammal_abundance_UW.txt
	
	
	What type of data should we record: let's say we went out and looked at animal abundances on Campus. Let's record what we saw:
	
	2013-02-26 Squirrel 5
	2013-02-26 Doves 7
	2013-02-26 Cats 8
	2013-02-26 Humans 4000
	
	
	(type info)
	cat mammal_abundance_UW.txt
	
	See file. Ok now what do we want to do with it?
	
	• Let's say we want to sort this by the abundance column from highest to lowest. Which is column 3 (but in unix would that be 2 right. We count starting at 0. 0,1,2)
	• We will use the command sort, we will specify what we want is in the 3rd column and we will tell unix that we want to sort by numbers
	
	sort -k 2 n mammal_abundance_UW.txt
	
	-get an output. 
	Ok cool we have sorted this file by abundance most to least. 
	
	We could also do it least to most:
	
	sort -k 2 n -r mammal_abundance_UW.txt
	
	This gives least to most. 
	
	If we wanted to do it alphabetically by the mammal names we could write:
	
	sort -k 1 mammal_abundance_UW.txt
	
	We can also do this on a comma-delimited files by using -t. We can find out many things about these unix commands on the internet, but also by going to the manual that comes with the programs. 
	
	man sort 
	
	(Read through file a bit, point out ways we could sort the file)
	
	Ok well let's say we wanted to save this sorted file to a new file. We will do that by typing:
	
	sort -k 1 mammal_abundance_UW.txt >  (what do we want to call this?)sorted_mammal_abundance_UW.txt
	
	ok notice that nothing appeared on the screen. This is because we are redirecting the output to the file. 
	
	Check to see if file is there:
	
	ls
	
	cat sorted_mammal_abundance_UW.txt
	
	Ok we have a new file with the sorted abundances. Cool. We can use this redirection with a number of commands to send the output to a new file. 

		
	Ok what if we wanted to find the top 2 most abundant  mammals and print out hat only that. We could use our sorted file and  a command called head. This is a useful command for quickly looking at the beginning of files. I use it to quickly check the beginning of large files (eg. how a fasta file from a sequencing run looks). 
	
	Test out what just plain head does:
	
	head sorted_mammal_abundance_UW.txt
	
	Should see all of the file since it is short.
	
	We can tell head that we only want  to see the top 2 lines:
	
	head -2 sorted_mammal_abundance_UW.txt
	
	
	(might seem confusing here that when we want 2 we actually say that, not like when we are counting  columns)
	
	gives us the first 2 lines. 
	
	so if we wanted to  to see the end of the file we could use something called tail:
	
	tail sorted_mammal_abundance_UW.txt
	
	Should give us everything. What if we wanted the last 2 lines of the file:
	
	tail -2 sorted_mammal_abundance_UW.txt
	
	Student exercise:  using our unsorted record of abundances  mammal_abundance_UW.txt find  the 2nd and 3rd most abundance organisms with their lines and print this to a new file. 


# Pipes and filters

## Objectives ##

- Write wildcard expressions that select certain subsets of the files in one or more directories.
- Explain when wildcards are expanded.
- Redirect a command's output to a file.
- Process a file instead of keyboard input using redirection.
- Construct command pipelines with two or more stages.
- Explain what usually happens if a program or pipeline isn't given any input to process.
- Explain Unix's "small pieces, loosely joined" philosophy.

### Duration: 20-30 minutes. ###



Now that we know a few basic commands, we can finally look at its most powerful feature: the ease with which it lets you combine existing programs in new ways. We'll start with a directory called "observations"

Let's create 3 files. Temperature observations in Vancouver, Iqaluit, St. John's Newfoundland. Do 5 for Vancouver, 2 for Iqaluit and 4 for St John's

    $ ls molecules
    temperature_observations_Vancouver.txt temperature_observations_Iqaluit.txt
    temperature_observations_StJohns.txt
    $

Let's go into that directory with `cd` and run the command `wc *.txt`. `wc` is the "word count" command: it counts the number of lines, words, and characters in files. The * in *.txt matches zero or more characters, so the shell turns *.txt into a complete list of .txt files:

    $ cd molecules
    $ wc *.txt
      20  156 1158 cubane.pdb
      12   84  622 ethane.pdb
       9   57  422 methane.pdb
      30  246 1828 octane.pdb
      21  165 1226 pentane.pdb
      15  111  825 propane.pdb
     107  819 6081 total
    $

Wildcards

* is a wildcard. It matches zero or more characters, so *.pdb matches ethane.pdb, propane.pdb, and so on. On the other hand, p*.pdb only matches pentane.pdb and propane.pdb, because the 'p' at the front only matches itself.

? is also a wildcard, but it only matches a single character. This means that p?.pdb matches pi.pdb or p5.pdb, but not propane.pdb. We can use any number of wildcards at a time: for example, p*.p?* matches anything that starts with a 'p' and ends with '.', 'p', and at least one more character (since the '?' has to match one character, and the final '*' can match any number of characters). Thus, p*.p?* would match preferred.practice, and even p.pi (since the first '*' can match no characters at all), but not quality.practice (doesn't start with 'p') or preferred.p (there isn't at least one character after the '.p').

When the shell sees a wildcard, it expands it to create a list of filenames before passing those names to whatever command is being run. This means that commands like wc and ls never see the wildcard characters, just what those wildcards matched. This is another example of orthogonal design.

If we run `wc -l` instead of just `wc`, the output shows only the number of lines per file:

    $ wc -l *.txt
      20  cubane.pdb
      12  ethane.pdb
       9  methane.pdb
      30  octane.pdb
      21  pentane.pdb
      15  propane.pdb
     107  total
    $

We can also use `-w` to get only the number of words, or `-c` to get only the number of characters.

Now, which of these files is shortest? It's an easy question to answer when there are only six files, but what if there were 6000? That's the kind of job we want a computer to do.

Our first step toward a solution is to run the command:

`$ wc -l *.pdb > lengths`

The `>` tells the shell to redirect the command's output to a file instead of printing it to the screen. The shell will create the file if it doesn't exist, or overwrite the contents of that file if it does. (This is why there is no screen output: everything that wc would have printed has gone into the file lengths instead.)

ls lengths confirms that the file exists:

    $ ls lengths
    lengths
    $

We can now send the content of lengths to the screen using `cat lengths`. `cat` stands for "concatenate": it prints the contents of files one after another. In this case, there's only one file, so cat just shows us what it contains:

    $ cat lengths
      20  cubane.pdb
      12  ethane.pdb
       9  methane.pdb
      30  octane.pdb
      21  pentane.pdb
      15  propane.pdb
     107  total
    $

Now let's use the sort command to sort its contents. This does not change the file. Instead, it sends the sorted result to the screen:

    $ sort lengths
      9  methane.pdb
     12  ethane.pdb
     15  propane.pdb
     20  cubane.pdb
     21  pentane.pdb
     30  octane.pdb
    107  total
    $

We can put the sorted list of lines in another temporary file called sorted-lengths by putting > sorted-lengths after the command, just as we used > lengths to put the output of wc into lengths. Once we've done that, we can run another command called head to get the first few lines in sorted-lengths:

    $ sort lengths > sorted-lengths
    $ head -1 sorted-lengths
      9  methane.pdb
    $

Giving head the parameter `-1` tells us we only want the first line of the file; `-20` would get the first 20, and so on. Since sorted-lengths the lengths of our files ordered from least to greatest, the output of head must be the file with the fewest lines.

If you think this is confusing, you're in good company: even once you understand what wc, sort, and head do, all those intermediate files make it hard to follow what's going on. How can we make it easier to understand?

Let's start by getting rid of the sorted-lengths file by running sort and head together:

    $ sort lengths | head -1
      9  methane.pdb
    $

The vertical bar between the two commands is called a pipe. It tells the shell that we want to use the output of the command on the left as the input to the command on the right. The computer might create a temporary file if it needs to, or copy data from one program to the other in memory, or something else entirely: we don't have to know or care.

Well, if we don't need to create the temporary file sorted-lengths, can we get rid of the lengths file too? The answer is "yes": we can use another pipe to send the output of wc directly to sort, which then sends its output to head:

    $ wc -l *.txt | sort | head -1
      9  methane.pdb
    $

This is exactly like a mathematician nesting functions like sin(πx)2 and saying "the square of the sine of x times π": in our case, the calculation is "head of sort of word count of *.txt".

### Inside Pipes ###

Here's what actually happens behind the scenes when we create a pipe. When a computer runs a program—any program—it creates a process in memory to hold the program's software and its current state. Every process has an input channel called standard input. (By this point, you may be surprised that the name is so memorable, but don't worry: most Unix programmers call it stdin.) Every process also has a default output channel called standard output, or stdout (Figure 11).
A Process with Standard Input and Output Figure 11: A Process with Standard Input and Output

The shell is just another program, and runs in a process like any other. Under normal circumstances, whatever we type on the keyboard is sent to the shell on its standard input, and whatever it produces on standard output is displayed on our screen (Figure 12):


When we run a program, the shell creates a new process. It then temporarily sends whatever we type on our keyboard to that process's standard input, and whatever the process sends to standard output to the screen (Figure 13):


Here's what happens when we run `wc -l *.txt > lengths`. The shell starts by telling the computer to create a new process to run the wc program. Since we've provided some filenames as parameters, wc reads from them instead of from standard input. And since we've used > to redirect output to a file, the shell connects the process's standard output to that file (Figure 14).
Running One Program with Redirection Figure 14: Running One Program with Redirection

If we run wc -l *.txt | sort instead, the shell creates two processes, one for each process in the pipe, so that wc and sort run simultaneously. The standard output of wc is fed directly to the standard input of sort; since there's no redirection with >, sort's output goes to the screen (Figure 15):

And if we run `wc -l *.txt | sort | head -1`, we get the three processes shown in Figure 16 with data flowing from the files, through wc to sort, and from sort through head to the screen.


This simple idea is why Unix has been so successful. Instead of creating enormous programs that try to do many different things, Unix programmers focus on creating lots of simple tools that each do one job well, and work well with each other. Ten such tools can be combined in 100 ways, and that's only looking at pairings: when we start to look at pipes with multiple stages, the possibilities are almost uncountable.

This programming model is called pipes and filters. We've already seen pipes; a filter is a program that transforms a stream of input into a stream of output. Almost all of the standard Unix tools can work this way: unless told to do otherwise, they read from standard input, do something with what they've read, and write to standard output.

The key is that any program that reads lines of text from standard input, and writes lines of text to standard output, can be combined with every other program that behaves this way as well. You can and should write your programs this way, so that you and other people can put those programs into pipes to multiply their power.
### Redirecting Input ###

As well as using > to redirect a program's output, we can use < to redirect its input, i.e., to read from a file instead of from standard input. For example, instead of writing `wc ammonia.pdb`, we could write `wc < ammonia.pdb`. In the first case, wc gets a command line parameter telling it what file to open. In the second, wc doesn't have any command line parameters, so it reads from standard input, but we have told the shell to send the contents of ammonia.pdb to wc's standard input.
Nelle's Pipeline: Checking Files

Nelle has run her samples through the assay machines and created 1520 files in the north-pacific-gyre/2012-07-03 directory described earlier. As a quick sanity check, she types:

    $ cd north-pacific-gyre/2012-07-03
    $ wc -l *.txt

The output is 1520 lines that look like this:

     300 NENE01729A.txt
     300 NENE01729B.txt
     300 NENE01736A.txt
     300 NENE01751A.txt
     300 NENE01751B.txt
     300 NENE01812A.txt
     ... ...

Now she types this:

    $ wc -l *.txt | sort | head -5
     240 NENE02018B.txt
     300 NENE01729A.txt
     300 NENE01729B.txt
     300 NENE01736A.txt
     300 NENE01751A.txt
    
Whoops: one of the files is 60 lines shorter than the others. When she goes back and checks it, she sees that she did that assay at 8:00 on a Monday morning—someone was probably in using the machine on the weekend, and she forgot to reset it. Before re-running that sample, she checks to see if any files have too much data:

    $ wc -l *.txt | sort | tail -5
     300 NENE02040A.txt
     300 NENE02040B.txt
     300 NENE02040Z.txt
     300 NENE02043A.txt
     300 NENE02043B.txt

Those numbers look good—but what's that 'Z' doing there in the third-to-last line? All of her samples should be marked 'A' or 'B'; by convention, her lab uses 'Z' to indicate samples with missing information. To find others like it, she does this:

    $ ls *Z.txt
    NENE01971Z.txtNENE02040Z.txt

Sure enough, when she checks the log on her laptop, there's no depth recorded for either of those samples. Since it's too late to get the information any other way, she must exclude those two files from her analysis. She could just delete them using rm, but there are actually some analyses she might do later where depth doesn't matter, so instead, she'll just be careful later on to select files using the wildcard expression `*[AB].txt`. As always, the '*' matches any number of characters; the new expression [AB] matches either an 'A' or a 'B', so this matches all the valid data files she has.

### Exercises ###


#### Exercise 2 ####

 What is the difference between:

wc -l < *.dat

and:

wc -l *.dat

#Find

## Objectives ##

-     Use grep to select lines from text files that match simple patterns.
-     Use find to find files whose names match simple patterns.
-     Use the output of one command as the command-line parameters to another command.
-     Explain what is meant by "text" and "binary" files, and why many common tools don't handle the latter well.

### Duration: 15 minutes. ###

You can often guess someone's age by listening to how people talk about search . Just as young people use "Google" as a verb, crusty old Unix programmers use "grep". The word is a contraction of "global/regular expression/print", a common sequence of operations in early Unix text editors. It is also the name of a very useful command-line program.

grep finds and prints lines in files that match a pattern. For our examples, we will use a file that contains three haikus taken from a 1998 competition in Salon magazine:

    The Tao that is seen
    Is not the true Tao, until
    You bring fresh toner.
    
    With searching comes loss
    and the presence of absence:
    "My Thesis" not found.
    
    Yesterday it worked
    Today it is not working
    Software is like that.

Let's find lines that contain the word "not":

    $ grep not haiku.txt
    Is not the true Tao, until
    "My Thesis" not found
    Today it is not working
    $

Here, not is the pattern we're searching for. It's pretty simple: every alphanumeric character matches against itself. After the pattern comes the name or names of the files we're searching in. The output is the three lines in the file that contain the letters "not".

Let's try a different pattern: "day".

    $ grep day haiku.txt
    Yesterday it worked
    Today it is not working
    $

This time, the output is lines containing the words "Yesterday" and "Today", which both have the letters "day". If we give grep the -w flag, it restricts matches to word boundaries, so that only lines with the word "day" will be printed:

    $ grep -w day haiku.txt
    $

In this case, there aren't any, so grep's output is empty.

Another useful option is `-n`, which numbers the lines that match:

    $ grep -n it haiku.txt
    5:With searching comes loss
    9:Yesterday it worked
    10:Today it is not working
    $

Here, we can see that lines 5, 9, and 10 contain the letters "it".

As with other Unix commands, we can combine flags. For example, since `-i` makes matching case-insensitive, and `-v` inverts the match, using them both only prints lines that don't match the pattern in any mix of upper and lower case:
    
    $ grep -i -v the haiku.txt
    You bring fresh toner.

	With searching comes loss

	Yesterday it worked
	Today it is not working
	Software is like that.
	$

grep has lots of other options. To find out what they are, we can type `man grep`. man is the Unix "manual" command. It prints a description of a command and its options, and (if you're lucky) provides a few examples of how to use it: OR for git bash you type `grep --help`
    
    $ man grep
    GREP(1)  GREP(1)
    
    NAME
       grep, egrep, fgrep - print lines matching a pattern
    
    SYNOPSIS
       grep [OPTIONS] PATTERN [FILE...]
       grep [OPTIONS] [-e PATTERN | -f FILE] [FILE...]
    
    DESCRIPTION
       grep  searches the named input FILEs (or standard input if no files are named, or if a single hyphen-
       minus (-) is given as file name) for lines containing a match to the given PATTERN.  By default, grep
       prints the matching lines.
       ………
    
    OPTIONS
       Generic Program Information
       --help Print  a  usage  message  briefly summarizing these command-line options and the bug-reporting
      address, then exit.
    
       -V, --version
      Print the version number of grep to the standard output stream.  This version number should be
      included in all bug reports (see below).
    
       Matcher Selection
       -E, --extended-regexp
      Interpret  PATTERN  as  an  extended regular expression (ERE, see below).  (-E is specified by
      POSIX.)
    
       -F, --fixed-strings
      Interpret PATTERN as a list of fixed strings, separated by newlines, any of  which  is  to  be
      matched.  (-F is specified by POSIX.)
    ………
    
## Wildcards ##

grep's real power doesn't come from its options, though; it comes from the fact that patterns can include wildcards. (The technical name for these is regular expressions, which is what the "re" in "grep" stands for.) Regular expressions are complex enough that we devoted an entire section of the website to them; if you want to do complex searches, please check it out. As a taster, we can find lines that have an 'o' in the second position like this:

    $ grep -E '^.o' haiku.txt
    You bring fresh toner.
    Today it is not working
    Software is like that.
    
We use the `-E` flag and put the pattern in quotes to prevent the shell from trying to interpret it. (If the pattern contained a '*', for example, the shell would try to expand it before running grep.) *Discuss this further......Shell expands it at the command line?? "With expansion, you type something and it is expanded into something else before the shell acts upon it. When the enter key is pressed, the shell automatically expands any qualifying characters on the command line before the command is carried out, so the echo command never saw the “*”, only its expanded result." The '^' in the pattern anchors the match to the start of the line. The '.' matches a single character (just like '?' in the shell), while the 'o' matches an actual 'o'.

While grep finds lines in files, the find command finds files themselves. Again, it has a lot of options; to show how the simplest ones work, we'll use the directory tree in Figure 18:
Sample Files and Directories Figure 18: Sample Files and Directories

Julia's home directory contains one file called notes.txt and four subdirectories: thesis (which is sadly empty), data (which contains two files first.txt and second.txt), a tools directory that contains the programs format and stats, and an empty subdirectory called old.

For our first command, let's run find . -type d. . is the directory where we want our search to start; -type d means "things that are directories". Sure enough, find's output is the names of the five directories in our little tree (including ., the current working directory):

    $ find . -type d
    ./
    ./data
    ./thesis
    ./tools
    ./tools/old
    $

If we change -type d to -type f, we get a listing of all the files instead:

    $ find . -type f
    ./data/first.txt
    ./data/second.txt
    ./notes.txt
    ./tools/format
    ./tools/stats
    $

find automatically goes into subdirectories, their subdirectories, and so on to find everything that matches the pattern we've given it. If we don't want it to, we can use -maxdepth to restrict the depth of search:

    $ find . -maxdepth 1 -type f
    ./notes.txt
    $
    
The opposite of -maxdepth is -mindepth, which tells find to only report things that are at or below a certain depth. `-mindepth 2` therefore finds all the files that are two or more levels below us:

    $ find . -mindepth 2 -type f
    ./data/first.txt
    ./data/second.txt
    ./tools/format
    ./tools/stats
    $

Another option is -empty, which restricts matches to empty files and directories:

    $ find . -empty
    ./thesis
    ./tools/old
    $

Now let's try matching by name:

    $ find . -name *.txt
    ./notes.txt
    $

We expected it to find all the text files, but it only prints out ./notes.txt. The problem is that the shell expands wildcard characters like * before commands run. Since *.txt in the current directory expands to notes.txt, the command we actually ran was:
    
    $ find . -name notes.txt

find did what we asked; we just asked for the wrong thing.

To get what we want, let's do what we did with grep: put *.txt in single quotes to prevent the shell from expanding the * wildcard. This way, find actually gets the pattern *.txt, not the expanded filename notes.txt:

    $ find . -name '*.txt'
    ./data/first.txt
    ./data/second.txt
    ./notes.txt
    $

As we said earlier, the command line's power lies in combining tools. We've seen how to do that with pipes; let's look at another technique. As we just saw, find . -name '*.txt' gives us a list of all text files in or below the current directory. How can we combine that with wc -l to count the lines in all those files?

One way is to put the find command inside $():

    $ wc -l $(find . -name '*.txt')
      70  ./data/first.txt
     420  ./data/second.txt
      30  ./notes.txt
     520  total
    $

When the shell executes this command, the first thing it does is run whatever is inside the $(). It then replaces the $() expression with that command's output. Since the output of find is the three filenames ./data/first.txt, ./data/second.txt, and ./notes.txt, the shell constructs the command:
    
    $ wc -l ./data/first.txt ./data/second.txt ./notes.txt

which is what we wanted. This expansion is exactly what the shell does when it expands wildcards like * and ?, but lets us use any command we want as our own "wildcard".

It's very common to use find and grep together. The first finds files that match a pattern; the second looks for lines inside those files that match another pattern. Here, for example, we can find PDB files that contain iron atoms by looking for the string "FE" in all the .pdb files below the current directory:

    $ grep FE $(find . -name '*.pdb')
    ./human/heme.pdb:ATOM  25  FE  1  -0.924  0.535  -0.518
    $
    
Binary Files

We have focused exclusively on finding things in text files. What if your data is stored as images, in databases, or in some other format? One option would be to extend tools like grep to handle those formats. This hasn't happened, and probably won't, because there are too many formats to support.

The second option is to convert the data to text, or extract the text-ish bits from the data. This is probably the most common approach, since it only requires people to build one tool per data format (to extract information). On the one hand, it makes simple things easy to do. On the negative side, complex things are usually impossible. For example, it's easy enough to write a program that will extract X and Y dimensions from image files for grep to play with, but how would you write something to find values in a spreadsheet whose cells contained formulas?

The third choice is to recognize that the shell and text processing have their limits, and to use a programming language such as Python instead. When the time comes to do this, don't be too hard on the shell: many modern programming languages, Python included, have borrowed a lot of ideas from it, and imitation is also the sincerest form of praise.
Nelle's Pipeline: The Second Stage

Nelle now has a directory called north-pacific-gyre/2012-07-03 containing 1518 data files, and needs to compare each one against all of the others to find the hundred pairs with the highest pairwise scores. Armed with what she has learned so far, she writes the following script

# Compare all pairs of files.
	for left in $*
		do
    	for right in $*
    	do
     	   echo $left $right $(goodiff $left $right)
    	done
	done

The outermost loop assigns the name of each file to the variable left in turn. The inner loop does the same thing for the variable right each time the outer loop executes, so inside the inner loop, left and right are given each pair of filenames.

Each time it runs the command inside the inner loop, the shell starts by running goodiff on the two files in order to expand the $() expression. Once it's done that, it passes the output, along with the names of the files, to echo. Thus, if Nelle saves this script as pairwise.sh and runs it as:
    
    $ bash pairwise.sh stats-*.txt

the shell runs:

    echo stats-NENE01729A.txt stats-NENE01729A.txt $(goodiff stats-NENE01729A.txt stats-NENE01729A.txt)
    echo stats-NENE01729A.txt stats-NENE01729B.txt $(goodiff stats-NENE01729A.txt stats-NENE01729B.txt)
    echo stats-NENE01729A.txt stats-NENE01736A.txt $(goodiff stats-NENE01729A.txt stats-NENE01736A.txt)
...

which turns into:

    echo stats-NENE01729A.txt stats-NENE01729A.txt files are identical
    echo stats-NENE01729A.txt stats-NENE01729B.txt 0.97182
    echo stats-NENE01729A.txt stats-NENE01736A.txt 0.45223
    ...
    
which in turn prints:

    stats-NENE01729A.txt stats-NENE01729A.txt files are identical
    stats-NENE01729A.txt stats-NENE01729B.txt 0.97182
    stats-NENE01729A.txt stats-NENE01736A.txt 0.45223
    ...

That's a good start, but Nelle can do better. First, she notices that when the two input files are the same, the output is the words "files are identical" instead of a numerical score. She can remove these lines like this:

    $ bash pairwise.sh stats-*.txt | grep -v 'files are identical'

or put the call to grep inside the shell script (which will be less error-prone):

    for left in $*
   	 do
    	for right in $*
    	do
    	echo $left $right $(goodiff $left $right)
    	done
    done | grep -v 'files are identical'

This works because do…done counts as a single command in Bash. If Nelle wanted to make this clearer, she could put parentheses around the loop:

    (for left in $*
    	do
    		for right in $*
    			do
    				echo $left $right $(goodiff $left $right)
    			done
    	done) | grep -v 'files are identical'

The last thing Nelle needs to do before writing up is find the 100 best pairwise matches. She has seen this before: sort the lines numerically, then use head to select the top lines. However, the numbers she wants to sort by are at the end of the line, rather than beginning. Reading the output of man sort tells her that the -k flag will let her specify which column of input she wants to use as a sort key, but the syntax looks a little complicated. Instead, she moves the score to the front of each line:

    (for left in $*
    	do
    		for right in $*
    			do
    				echo $(goodiff $left $right) $left $right
    			done
    	done) | grep -v 'files are identical'

and then adds two more commands to the pipeline:

    (for left in $*
    	do
    		for right in $*
    			do
    				echo $(goodiff $left $right) $left $right
    			done
    	done) | grep -v 'files are identical' | sort -n -r | head -100

Since this is hard to read, she uses \ to tell the shell that she's continuing commands on the next line:

    (for left in $*
    	do
    		for right in $*
    			do
    				echo $(goodiff $left $right) $left $right
    			done
    	done) \
    | grep -v 'files are identical' \
    | sort -n -r \
    | head -100

She then runs:
    
    $ bash pairwise.sh stats-*.txt > top100.txt

and heads off to a seminar, confident that by the time she comes back tomorrow, top100.txt will contain the results she needs for her paper.

	Ok and before we get too ahead of ourselves it is great that we can use the up arrow to scroll through the past commands that we have used:
	
	history
	
	If we want we can send the print out of this command to a file. Good for our record keeping:
	
	history > command_log_2013_02_26.txt

	
	(cut -d, -f 1 data.txt
	cut by delimeter: "," so can choose the appropriate columns
	select only the word  squirrel)
	

	
	wc -l  mammal_abundance_UW.txt, mammal_abundance_UBC.txt
	
	But how can I do this more efficiently rather than repeating this command for each file (going to make a mistake!)? I can use a wildcard to expand to multiple files.  
	wildcards- eg * to expand to all matching 
	explain the expansion
			
	first test what this asterisk will give us
	
	ls *.* 
	(should give us all of the files in our directory)
	
	ls *.txt 
	(should give us all the text files)
	
	ls  mammal_abundance_*.txt
	 (should give us the abundance count log files and no others. Important to check to make sure it is working as you expect)
	
	wc -l mammal_abundance_*.txt
	
	(Could I have one more file and I could show  how to use "."?)

### Exercises ###

#### Exercise 1 ####
 Write a short explanatory comment for the following shell script:

find . -name '*.dat' -print | wc -l | sort -n


### Other exercises--Optional. To be removed or edited down.  ###

# Shell

Let's try out your new shell skills on some real data.

The file `1000gp.vcf` is a small sample (1%) of a very large text file
containing human genetics data. Specifically, it describes genetic variation in
three African individuals sequenced as part of the [1000 Genomes
Project](http://www.1000genomes.org). 

## Exercise Part 1 (setup)

* If you had forgotten where you downloaded the file, how would you locate the
path of all files with that name on the computer (using the shell)?  

  **Hint:**
  > `$ man find`

  **Answer:**
  > `$ find / -name "1000gp.vcf"`

* It's usually a good idea to use an empty directory as a workspace so that
  other files don't get in the way (or accidentally get overwritten or deleted).
  Create a new subdirectory directory named "sandbox", move our data file there,
  and make the directory your current working directory (sandbox should be the
  last part of the path given when you type `pwd`. 


  **Answer:**
  > ```bash
  > $ mkdir sandbox
  > $ mv /home/orion/Downloads/1000gp.vcf sandbox
  > $ cd sandbox
  > ```


## Exercise Part 2 (analysis)

* The data file you downloaded is a line-based text file. The "vcf" extension
  lets us know that it's in a specific text format, namely "Variant Call
  Format". The file starts with a bunch of comment lines (they start with "#" or
  "##"), and then a large number of data lines. The human genome can be thought
  of as an encyclopedia, where each chromosome is a volume. Each volume is just
  a long string of characters, but rather than the english alphabet, the genome
  uses just the characters "A", "C", "G", and "T". This VCF file lists the
  differences between the three African individuals and a standard "individual"
  called the reference (actually based upon a few different people). Each line
  in the file corresponds to a difference. The line tells us the position of the
  difference (chromosome and position), the genetic sequence in the reference,
  and the corresponding sequence in each of the three Africans. Research is
  ongoing to understand the full effects of these genetic differences; some
  cause diseases such as Tay-Sachs and Hemophilia, while others determine your
  blood type and eye color.

  Before we start processing the file, let's get a high-level view of the file
  that we're about to work with.

  What's the file size (in kilo-bytes), and how many lines are in the file?


  **Hint:**
  > There's an option to `ls` that will print the file sizes in a more
  > human-friendly format.


  **A hint about the number of lines:**
  > `$ man wc`


  **Answer:**
  > We should get a file size around 3.6 MB with:
  > `$ ls -lh 1000gp.vcf`
  > Alternatively, the command `du` can be used to achieve a similar result:
  > `$ du -h 1000gp.vcf`
  > 
  > We find there are 45034 lines with:
  > `$ wc -l 1000gp.vcf`


* Because this file is so large, you're going to almost always want to pipe
("|") the result of any command to `less` (a simple text viewer, type 'q' to
exit) or `head` (to print the first 10 lines) so that you don't accidentally
print 45,000 lines to the screen.

  Let's start by printing the first 5 lines to see what it looks like.  

  **Answer:**
  > `$ head -5 1000gp.vcf`

* That isn't very interesting; it's just a bunch of the comments at the
beginning of the file (they all start with "#")! Print the first 20 lines to see
more of the file.

  **Answer:**
  > `$ head -20 1000gp.vcf`


* Okay, so now we can see the basic structure of the file. A few comment lines
  that start with "#" or "##" and then a bunch of lines of data that contain all
  the data and are pretty hard to understand. Each line of data contains the
  same number of fields, and all fields are separated with TABs. These fields
  are:

  1. the chromosome (which volume the difference is in)
  2. the position (which character in the volume the difference starts at)
  3. the ID of the difference
  4. the sequence in the reference human(s)

  The rest of the columns tell us, in a rather complex way, a bunch of
  additional information about that position, including: the predicted sequence
  for each of the three Africans and how confident the scientists are that these
  sequences are correct.

  To start analyzing the actual data, we have to remove the header. How can we
  print the first 10 non-header lines (those that _don't_ start with a "#")?

  **Hint:**
    $ man grep

  **Hint:**
  > You can use a pipe ("|") to connect the output of `grep` to the input of
  > `head`.

  **Hint:**
  In `grep` regular expressions, the carat '^' character matches the start of a
  line and the dollar sign '$' matches the end of a line. Thus, the following
  will print all non-blank lines from `file`:
    $ grep -v "^$" file

  **Our answer:**
  >     $ grep -v "^#" 1000gp.vcf | head
  > 
  > Why are neither of these correct?
  >     $ grep -v "#" 1000gp.vcf | head
  >     $ grep -v "^##" 1000gp.vcf | head

* How many lines of data are in the file (rather than counting the number of
  header lines and subtracting, try just counting the number of data lines)?

  **Hint:**
  > Instead of piping to `head`, try piping to `wc`.

  **Our Answer:**
  >     $ grep -v "^#" 1000gp.vcf | wc -l
  >
  > should print `45024`

* Where these differences are located can be important. If all the differences
  between two encyclopedias were in just the first volume, that would be
  interesting. The first field of each data line is the name of the chromosome
  that the difference occurs on (which volume we're on). Print the first 10
  chromosomes, one per line.

  **Hint:**
  > You can extract a column from a tab-delimited text file using the `cut`
  > command.

  **Hint:**
  > Use `grep` to print only non-comment lines, and `cut` to extract the
  > chromosome column.

  **Our Answer:**
  >     $ grep -v "^#" 1000gp.vcf | cut -f 1 | head

* As you should have observed, the first 10 lines are on numbered chromosomes.
  Every normal cell in your body has 23 pairs of chromosomes, 22 pairs of
  "autosomal" chromosomes (these are numbered 1-22) and a pair of sex
  chromosomes (two Xs if you're female, an X and a Y if you're male). If you've
  heard of the genetics company [23andMe](https://www.23andme.com), the 23
  refers to these 23 pairs of chromosomes. 

  Let's look at which chromosomes these variations are on. Print a list of the
  chromosomes that are in the file (each chromosome name should only be printed
  once, so you should only print 23 lines).

  **Hint:**
  > You need to remove all the duplicate lines from your previous answer.

  **Hint:**
  > `sort` has an option that should make this easier.

  **Our Answer:**
  >     $ grep -v "^#" 1000gp.vcf | cut -f 1 | sort -u


* Rather than using `sort` to print unique results, a common pipeline is to
  first sort and then pipe to another UNIX command, `uniq`. The `uniq` command
  takes _sorted_ input and prints only unique lines, but it provides more
  flexibility than just using `sort` by itself. Keep in mind, if the input isn't
  sorted, `uniq` won't work properly.

  Using `sort` and `uniq`, print the number of times each chromosome occurs in
  the file.

  **Hint:**
  >     $ man uniq

  **Hint:**
  > Instead of using `sort` to remove duplicates, just use it to sort and pipe
  > the result to `uniq`.

  **Our Answer:**
  >     $ grep -v "^#" 1000gp.vcf | cut -f 1 | sort | uniq -c


* Add to your previous solution to list the chromosomes from most frequently
  observed to least frequently observed.

  **Hint:**
  >     $ man sort

  **Hint:**
  > Make sure you're sorting in descending order. By default, `sort` sorts in
  > ascending order.

  **Our Answer:**
  >     $ grep -v "^#" 1000gp.vcf | cut -f 1 | sort | uniq -c | sort -n -r
  >
  > should output the following:
  >
  >     3721 2
  >     3387 1
  >     3224 4
  >     3219 3
  >     2894 5
  >     2860 6
  >     2527 8
  >     2525 7
  >     2203 10
  >     2166 11
  >     2032 12
  >     1865 9
  >     1656 13
  >     1409 14
  >     1362 16
  >     1304 X
  >     1275 18
  >     1265 15
  >     1097 17
  >      993 20
  >      814 19
  >      661 21
  >      565 22
    
* The autosomal chromosomes (1-22) are named according to their size. The
  largest of them is chromosome 1, while the smallest is chromosome 22. Does it
  look like differences occur relatively randomly across the genome, or are some
  chromosomes more different than you'd expect at random (very roughly taking
  their sizes into account)?

  It's worth noting that the chromosomes were numbered by the sizes of the
  actual molecules, not how much of them had been sequenced.

  Wikipedia has a nice table of chromosome sizes and how much of each has been
  sequenced (and you can sort it):
  http://en.wikipedia.org/wiki/Human_chromosome#Human_chromosomes

  Notice anything?

  **Our Hypothesis:**
  > Since variation can only be found in the known sequence, the order you
  > printed corresponds closely to ordering by the number of bases sequenced
  > (rather than the total number of bases). 
  > 
  > Given this, it seems like differences occur relatively randomly across the
  > genome. We see more differences on longer chromosomes, fewer on shorter,
  > without any striking outliers.

* This is great, but biologists might also like to see the chromosomes ordered
  by their number (not dictionary order), since different chromosomes have
  different attributes and this ordering allows them to find a specific
  chromosome more easily.

  **Hint:**
  > A lot of the power of `sort` comes from the fact that you can specify which
  > fields to sort on, and the order in which to sort them. In this case you
  > only need to sort on one field.

  **Answer:**
  >     $ grep -v "^#" 1000gp.vcf | cut -f 1 | sort | uniq -c | sort -k 2n

