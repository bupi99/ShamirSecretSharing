This is a working implementation of Shamir's Secret Sharing Scheme.
We utilize the secrets library for python, which may need to be installed.
This should be able to be run on any platform, but we have only tested it on Windows 10.

To use complete the following steps:

First select/create up to 250 destination folders, within those folders create a new file, where the partial secrets will be stored.

Now Run the command 
python "SM Encrypting.py" n k f_path_source f_path_dest1 f_path_dest2 ... f_path_destn

Where f_path_source, is the path to the file which we will be sharing amoung the destinations.
Likewise f_path_dest* are the paths to the files created in the first step.

