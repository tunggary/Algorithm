def parsingProcess(process):
  data = process.split()
  return data[0], list(map(int, data[1:]))

def working(arr, result, process):
  if process[0] == 'read':
    result.append(arr[process[2]:process[3]+1])
  else:
    for i in range(process[1][2], process[1][3]+1):
      arr[i] = str(process[1][4])

def solution(arr, processes):
  data2 = parsingProcess(processes[0])
  workingProcess = [[ data2,1]]
  waitingProcess = []
  totalTime = 1
  result = []
  
  while workingProcess or waitingProcess:
    if processes:
      process = processes.pop(0)
      process = parsingProcess(process)
      if process[0] == 'write':
        if len(workingProcess) == 0:
          workingProcess.append([process, 1])
          working(arr, result, process)
        else:
          waitingProcess.append((process[0], process[1][0], process[1][1:]))
      else:
        if len(workingProcess) > 0:
          if workingProcess[0][0] == 'write':
            waitingProcess.append((process[0], process[1][0], process[1][1:]))
          else:
            workingProcess.append([process, 1])
        else:
          workingProcess.append([process, 1])
        
    for i in range(len(workingProcess)):
      info, data = workingProcess[i]
      print(data)
      if workingProcess[i][1] > workingProcess[i][0][1][1]:
        workingProcess.pop(i)
      else:
        workingProcess[i][1] += 1
    
    if waitingProcess:
      waitingProcess.sort(key=lambda x: (-x[0], x[1]))
      if len(workingProcess) > 0:
        if workingProcess[0][0] == 'read':
          process = waitingProcess.pop(0)
          workingProcess.append([(process[0], process[1]+process[2]),1])
      else:
        process = waitingProcess.pop(0)
        workingProcess.append([(process[0], process[1]+process[2]),1])
    totalTime += 1
  print(result, totalTime)
solution(["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"])
# arr = [1,2,3]
# arr.pop(1)
# print(arr)