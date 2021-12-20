'''
Code for parsing the zoom transcript or converting audio to text (if needed). Currently, I have coded parsing the zoom text.
'''


def get_file():
  '''
  Returns the content, the time stamps for each sentence and who said each sentence (N/A if zoom didn't pick it up).
  '''
  with open("recording.txt") as f:
    contents = f.readlines()

  times = []
  lines = []

  for i in range(len(contents)):
    if len(contents[i].split(" --> ")) == 2:
      times.append(contents[i].split(" --> "))
      if len(contents[i+1].split(": ")) == 2:
        lines.append(contents[i+1].split(": "))
      else:
        lines.append(["N/A", contents[i+1]])

  para = ""

  for line in lines:
    line[1] = line[1][:-2]
    para+=line[1] + " "

  return times,lines,para






