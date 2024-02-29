# This python script will get the program-as-data version of the quine,
#   as well as its output, normalize them (i.e. remove whitespace,
#   and convert all all 0's and []'s in the outputs of hwhile to nils),
#   and do a comparison between the two, printing the result.


from os import system


def normalize(prog_rep):
  
  # remove all whitespace from the output and source code
  prog_rep = prog_rep.replace('\r','')
  prog_rep = prog_rep.replace('\n','')
  prog_rep = prog_rep.replace(' ','')
  
  # make all 0's and empty lists represented by nils across the board
  prog_rep = prog_rep.replace('0','nil')
  prog_rep = prog_rep.replace('[]','nil')
  
  return prog_rep


# Run hwhile in unparser mode on quine.while to get the source code as data
system('hwhile -u quine.while >quine-source.txt')
quine_source = normalize(open('quine-source.txt','r+').read())

# Run hwhile on quine.while to get its output
system('hwhile -La quine.while [] >quine-output.txt')
quine_output = normalize(open('quine-output.txt','r+').read())

# Compare the two
print( quine_source == quine_output )